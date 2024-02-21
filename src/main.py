from time import sleep
from random import choice
import requests
import socks
import socket
from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
import random
import string
from selenium.webdriver.chrome.options import Options

logger.add(
    sink=lambda message: print(message, end=''),
    format='<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - {message}',
)


def check_proxy(proxy_host, proxy_port):
    socks.set_default_proxy(socks.SOCKS5, proxy_host, int(proxy_port))
    socket.socket = socks.socksocket
    try:
        response = requests.get('http://www.example.com')
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False


def filter_proxies(proxy_list):
    filtered_proxies = []
    for proxy in proxy_list:
        proxy_host, proxy_port = proxy.split(':')
        if check_proxy(proxy_host, proxy_port):
            filtered_proxies.append(proxy)
    return filtered_proxies


def create_ads_power_group() -> str:
    group = requests.post(
        'http://local.adspower.net:50325/api/v1/group/create',
        json={
            'group_name': ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8)),
        },
    ).json()
    return group['data']['group_id']


def create_ads_power_profile(host, port, group_id) -> str:
    create = requests.post(
        'http://local.adspower.net:50325/api/v1/user/create', 
        json={
            'group_id': group_id,
            'user_proxy_config': {
                'proxy_soft': 'other',
                'proxy_type': 'socks5',
                'proxy_host': host,
                'proxy_port': port,
            },
            'country': 'it',
            'ip_country': 'it',
            'fingerprint_config': {
                'ua': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36',
                'ua_system_version': ["Android"],
            },
        },
    ).json()
    return create['data']['id']


def create_credentials_dict() -> dict[str, str]:
    credentials_dict = {}
    with open('credentials.txt', 'r') as file:
        for line in file:
            email, password = line.strip().split(' ')
            credentials_dict[email] = password
    return credentials_dict


def create_proxy_list() -> list[str] | None:
    try:
        with open('proxy.txt', 'r') as f:
            proxie_choice = f.read().splitlines()
            return proxie_choice
    except Exception:
        logger.warning('Файл proxy.txt не найден')
        return None


def get_random_unused_proxy(proxy_list: list) -> str:
    if proxy_list:
        random_proxy = choice(proxy_list)
        proxy_list.remove(random_proxy)
        return random_proxy
    else:
        logger.warning('Отсутствуют доступные прокси')
        return None


def create_driver(proxy: str = None, profile_id: str = None) -> webdriver.Chrome:
    #options.add_argument("--headless")  # Run Chrome in headless mode
    open_url = f'http://local.adspower.net:50325/api/v1/browser/start?user_id={profile_id}'
    #close_url = f'http://local.adspower.net:50325/api/v1/browser/stop?user_id={profile_id}'

    response = requests.get(open_url).json()
    service = Service(response['data']['webdriver'])
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option("debuggerAddress", response['data']['ws']['selenium'])
    driver = webdriver.Chrome(
        service=service,
        options=options,
    )
    driver.get('https://it.wallapop.com/login')
    #requests.get(close_url)
    return driver


def register_user_account_in_it_wallapop(
        driver: webdriver.Chrome,
        email: str,
        password: str,
) -> None:
    try:
        driver.get(url='https://it.wallapop.com/login')
        sleep(20)
        try:
            driver.find_element(
                By.XPATH,
                '//button[@id="onetrust-accept-btn-handler" and contains(text(), "Accetta tutto")]',
            ).click()
            logger.info(f'{email} - приняты cookies')
        except Exception as exception:
            logger.warning(f'{email} - не найдено окно принятия cookies')
        finally:
            sleep(20)
        try:
            driver.find_element(By.XPATH, '//walla-button[1]').click()
            logger.info(f'{email} - начат вход google пользователя')
        except Exception as exception:
            logger.error(exception)
        finally:
            sleep(20)

        main_window_handle = driver.window_handles[0]
        child_window_handle = driver.window_handles[1]
        driver.switch_to.window(child_window_handle)
        logger.info(f'{email} - успешно открыто дочернее google oaut окно')
        sleep(20)

        try:
            driver.find_element(
                By.XPATH,
                '//input[@type="email"]',
            ).send_keys(email)
            driver.find_element(By.XPATH, '//span[text()="Next"]').click()
            logger.info(f'{email} - заполнено поле почты')
        except Exception as exception:
            logger.error(exception)
        finally:
            sleep(20)

        driver.find_element(
            By.XPATH,
            '//input[@type="password"]',
        ).send_keys(password)
        driver.find_element(By.XPATH, '//span[text()="Next"]').click()
        logger.info(f'{email} - заполнено поле пароля')
        sleep(20)

        try:
            driver.find_element(By.ID, 'confirm').click()
            logger.warning(f'{email} - Добро пожаловать в ваш новый аккаунт')
        except Exception as exception:
            pass
        finally:
            sleep(20)

        try:
            driver.find_element(By.XPATH, '//div[@id="confirm_yes"]').click()
            logger.info(f'{email} - подтверждён вход через google')
        except Exception as exception:
            logger.info(f'{email} - вероятно браузер не потребовал подтверждение входа через google')
            logger.error(exception)
        finally:
            sleep(20)

        driver.switch_to.window(main_window_handle)
        logger.info(f'{email} - вернулись к основному окну')
        sleep(20)

        try:
            driver.find_element(
                By.XPATH,
                '(//input[@type="checkbox"])[2]',
            ).click()
            driver.find_element(By.XPATH, '(//walla-button[1])[2]').click()
            logger.info(f'{email} - прочитано лицензионное соглашение')
        except Exception as exception:
            logger.error(exception)
        finally:
            sleep(20)
        logger.info(f'{email} - начинает ожидание длинной в 15 минут')
        return driver

    except Exception as exception:
        logger.error(exception)
    finally:
        driver.close()
        driver.quit()


credentials_dict = create_credentials_dict()
proxy_list = filter_proxies(create_proxy_list())
drivers = []
profile_ids = []
group_id = create_ads_power_group()
profile_id_counter = 0


for i in range(len(credentials_dict)):
    proxy_host, proxy_port = get_random_unused_proxy(proxy_list=proxy_list).split(':')
    profile_id = create_ads_power_profile(
        host=proxy_host,
        port=proxy_port,
        group_id=group_id,
    )
    profile_ids.append(profile_id)

for email, password in credentials_dict.items():
    drivers.append(
        register_user_account_in_it_wallapop(
            driver=create_driver(
                proxy=get_random_unused_proxy(
                    proxy_list=proxy_list,
                ),
                profile_id=profile_ids[profile_id_counter],
            ),
            email=email,
            password=password,
        )
    )
    profile_id_counter += 1

for driver in drivers:
    driver.close()
    driver.quit()
