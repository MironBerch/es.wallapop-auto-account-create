from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from loguru import logger
#logger.add(
    #sink=lambda message: print(message, end=''),
    #format='<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - {message}'
    #format='<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}</cyan> - {message}',
#)

#logger.add()#(sink=lambda message: print(message, end=''))
#from fake_useragent import UserAgent
#useragent = UserAgent(os='linux', browsers='chrome')
#options.add_argument(f'user-agent={useragent.random}')
email=''
password=''

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('user-agent=Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.3')

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:

    driver.get(url='https://es.wallapop.com/login')
    sleep(3)
    driver.find_element(
        By.XPATH,
        '//button[@id="onetrust-accept-btn-handler" and contains(text(), "Aceptar todo")]',
    ).click()
    logger.info('accepted cookies')
    sleep(2)
    driver.find_element(By.XPATH, '//walla-button[1]').click()
    logger.info('start register use google account')

    sleep(7)
    main_window_handle = driver.window_handles[0]
    child_window_handle = driver.window_handles[1]
    # Switch to the child window
    driver.switch_to.window(child_window_handle)
    logger.info('open google v3 oauth window')
    driver.find_element(By.XPATH, '//input[@type="email"]').send_keys(email)
    driver.find_element(By.XPATH, '//span[text()="Next"]').click()
    logger.info(f'input email - {email}')
    sleep(2)
    logger.info('start register use google account')
    driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(email)
    driver.find_element(By.XPATH, '//span[text()="Next"]').click()
    password_value = len(password) * '*'
    logger.info(f'input password - {password_value}')
    # Switch back to the main window
    #driver.switch_to.window(main_window_handle)
    #next_register_step.click()
    sleep(30)
except Exception as exception:
    logger.error(exception)
finally:
    driver.close()
    driver.quit()
