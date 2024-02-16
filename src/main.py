from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#from fake_useragent import UserAgent
#useragent = UserAgent(os='linux', browsers='chrome')
#options.add_argument(f'user-agent={useragent.random}')

options = webdriver.ChromeOptions()
#options.add_argument('user-agent=Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.3')

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get(url="https://es.wallapop.com/login")
    sleep(2)
    accept_cookies = driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler' and contains(text(), 'Aceptar todo')]")
    accept_cookies.click()
    google_login = driver.find_element(By.XPATH, '//walla-button[1]')
    google_login.click()
    sleep(30)
except Exception as exception:
    print(exception)
finally:
    driver.close()
    driver.quit()
