from time import sleep
from random import choice

from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from seleniumwire import webdriver, undetected_chromedriver
from webdriver_manager.chrome import ChromeDriverManager

logger.add(
    sink=lambda message: print(message, end=''),
    format='<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - {message}',
)


def create_credentials_dict() -> dict[str, str]:
    credentials_dict = {}
    with open('credentials.txt', 'r') as file:
        for line in file:
            email, password = line.strip().split(' ')
            credentials_dict[email] = password
    for email, password in credentials_dict.items():
        print(f'Email: {email}, Password: {password}')
    return credentials_dict

#обращения к почте для получения пароля
"""
email_to_lookup = 'QCj4s6BLecE8@houschool.com'
if email_to_lookup in credentials_dict:
    password_for_email = credentials_dict[email_to_lookup]
    print(f"Password for {email_to_lookup}: {password_for_email}")
else:
    print(f"Email {email_to_lookup} not found in the cred.")
"""

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


def create_driver(proxy: str = None) -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    #undetected_chromedriver.ChromeOptions()
    #options.add_argument("--proxy-server=https://192.168.0.102:30019") #192.168.0.102:30019")
    #proxy_options = {
    #    'proxy': {
    #        'https': f'https://{proxy}',
    #    }
    #}
    if proxy:
        options.add_argument('--proxy-type=socks5')
        options.add_argument('--proxy-server=socks5://' + proxy)
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Linux; Android 11; Pixel 4)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36'
    )
    options.add_argument('--ignore-certificate-errors')
    #options.add_argument("--headless")  # Run Chrome in headless mode
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(
        #seleniumwire_options=proxy_options,
        service=service,
        options=options,
    )
    return driver


def register_user_account_in_it_wallapop(
        driver: webdriver.Chrome,
        email: str,
        password: str,
) -> None:
    try:
        driver.get(url='https://it.wallapop.com/login')
        #driver.get(url="https://whoer.net/")
        sleep(10)
        try:
            driver.find_element(
                By.XPATH,
                '//button[@id="onetrust-accept-btn-handler" and contains(text(), "Accetta tutto")]',
            ).click()
            logger.info(f'{email} - приняты cookies')
        except Exception as exception:
            logger.warning(f'{email} - не найдено окно принятия cookies')
            logger.error(exception)
        finally:
            sleep(10)
        try:
            driver.find_element(By.XPATH, '//walla-button[1]').click()
            logger.info(f'{email} - начат вход google пользователя')
        except Exception as exception:
            logger.error(exception)
        finally:
            sleep(10)
        try:
            main_window_handle = driver.window_handles[0]
            child_window_handle = driver.window_handles[1]
            driver.switch_to.window(child_window_handle)
            logger.info(f'{email} - успешно открыто дочернее google oaut окно')
        except Exception as exception:
            logger.error(exception)
        finally:
            sleep(10)
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
            sleep(10)
        try:
            driver.find_element(
                By.XPATH,
                '//input[@type="password"]',
            ).send_keys(password)
            driver.find_element(By.XPATH, '//span[text()="Next"]').click()
            logger.info(f'{email} - заполнено поле пароля')
        except Exception as exception:
            logger.error(exception)
        finally:
            sleep(10)
        try:
            driver.find_element(By.XPATH, '//div[@id="confirm_yes"]').click()
            logger.info(f'{email} - подтверждён вход через google')
        except Exception as exception:
            logger.warning(f'{email} - вероятно браузер не потребовал подтверждение входа через google')
            logger.error(exception)
        finally:
            sleep(10)
        try:
            driver.switch_to.window(main_window_handle)
            logger.info(f'{email} - вернулись к основному окну')
        except Exception as exception:
            logger.error(exception)
        finally:
            sleep(10)
        try:
            driver.find_element(By.XPATH, '(//input[@type="checkbox"])[2]').click()
            driver.find_element(By.XPATH, '(//walla-button[1])[2]').click()
            logger.info(f'{email} - прочитано лицензионное соглашение')
        except Exception as exception:
            logger.error(exception)
        finally:
            sleep(10)
        logger.info(f'{email} - начинает ожидание длинной в 15 минут')
        sleep(15*60)
        logger.info(f'{email} - начинает ожидание длинной в 15 минут')
    except Exception as exception:
        logger.error(exception)
    finally:
        driver.close()
        driver.quit()


credentials_dict = create_credentials_dict()
proxy_list = create_proxy_list()

for email, password in credentials_dict.items():
    register_user_account_in_it_wallapop(
        driver=create_driver(
            proxy=get_random_unused_proxy(
                proxy_list=proxy_list,
            )
        ),
        email=email,
        password=password,
    )
