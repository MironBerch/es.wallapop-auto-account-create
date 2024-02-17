from time import sleep

from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from loguru import logger
logger.add(
    sink=lambda message: print(message, end=''),
    format='<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - {message}',
)

#from fake_useragent import UserAgent
#useragent = UserAgent(os='linux', browsers='chrome')
#options.add_argument(f'user-agent={useragent.random}')
email=''
password=''

options = webdriver.ChromeOptions()
# set proxy
options.add_argument("--proxy-server=192.168.0.102:30019")
#proxy_options = {
#    "proxy": {
#        "https": 'https://192.168.0.102:30019/',#'https://modeler_6eeKKg:Q2sPaMgDtfH8@192.168.0.102:30019'
#    }
#}
options.add_argument('--disable-blink-features=AutomationControlled')
#options.add_argument('user-agent=Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.3')
options.add_argument('--user-agent=Mozilla/5.0 (Linux; Android 11; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36')
#options.add_argument("--headless")  # Run Chrome in headless mode

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(
    service=service,
    #seleniumwire_options=proxy_options,
    options=options,
)

try:
    driver.get(url='https://it.wallapop.com/login')
    sleep(10)
    try:
        driver.find_element(
            By.XPATH,
            '//button[@id="onetrust-accept-btn-handler" and contains(text(), "Accetta tutto")]',
        ).click()
        logger.info('accepted cookies')
    except:
        pass
    sleep(2)
    driver.find_element(By.XPATH, '//walla-button[1]').click()
    logger.info('start register use google account')

    sleep(7)
    main_window_handle = driver.window_handles[0]
    child_window_handle = driver.window_handles[1]
    driver.switch_to.window(child_window_handle)
    logger.info('open google v3 oauth window')
    driver.find_element(By.XPATH, '//input[@type="email"]').send_keys(email)
    driver.find_element(By.XPATH, '//span[text()="Next"]').click()
    logger.info(f'input email - {email}')
    sleep(4)
    driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//span[text()="Next"]').click()
    password_value = len(password) * '*'
    logger.info(f'input password - {password_value}')
    sleep(7)
    try:
        driver.find_element(By.XPATH, '//div[@id="confirm_yes"]').click()
        logger.info('confirm login')
    except:
        logger.warning('window closed so early')
    sleep(7)
    try:
        driver.switch_to.window(main_window_handle)
        sleep(2)
    except:
        pass
    driver.find_element(By.XPATH, '(//input[@type="checkbox"])[2]').click()
    driver.find_element(By.XPATH, '(//walla-button[1])[2]').click()
    sleep(360)
except Exception as exception:
    logger.error(exception)
finally:
    driver.close()
    driver.quit()
