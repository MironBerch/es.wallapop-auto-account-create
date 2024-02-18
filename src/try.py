from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from seleniumwire import webdriver as wiredriver
import time
# Список IP адресов для проверки

def create_proxy_list() -> list[str] | None:
    try:
        with open('proxy.txt', 'r') as f:
            proxie_choice = f.read().splitlines()
            return proxie_choice
    except Exception:
        return None


ip_list = create_proxy_list()

"""
def check_proxy(proxy_address):
    try:
        # Проверка работы со стандартным прокси
        driver = wiredriver.Chrome()
        driver.get('https://2ip.ru/')
        time.sleep(5)
        driver.close()
        print(f"{proxy_address} работает с обычным прокси")

        # Проверка работы с SOCKS5
        options = {
            'proxy': {
                'address': proxy_address,
                'use_proxy': True,
                'no_proxy': 'localhost,127.0.0.1'  # Exclude localhost from proxying
            }
        }
        driver = wiredriver.Chrome(seleniumwire_options=options)
        driver.get('https://2ip.ru/')
        time.sleep(5)
        driver.quit()
        print(f"{proxy_address} работает с SOCKS5 прокси")

    except Exception as e:
        print(f"{proxy_address} не работает: {str(e)}")

# Проходимся по списку IP и проверяем их работоспособность
for ip in ip_list:
    check_proxy(ip)
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from seleniumwire import webdriver as wiredriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

def check_proxy(proxy_address):
    try:
        # Проверка работы с SOCKS5
        options = {
            'proxy': {
                'http': proxy_address,
                'https': proxy_address,
                'no_proxy': 'localhost,127.0.0.1'  # Exclude localhost from proxying
            }
        }
        driver = wiredriver.Chrome(seleniumwire_options=options)
        driver.get('https://2ip.ru/')
        time.sleep(5)
        driver.quit()
        print(f"{proxy_address} работает с SOCKS5 прокси")

    except Exception as e:
        print(f"{proxy_address} не работает: {str(e)}")

# Проходимся по списку IP и проверяем их работоспособность
for ip in ip_list:
    check_proxy(ip)
