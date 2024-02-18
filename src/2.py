from time import sleep

from loguru import logger
#from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from seleniumwire import webdriver, undetected_chromedriver as ec
from webdriver_manager.chrome import ChromeDriverManager


def create_driver(proxy: str) -> webdriver.Chrome:
    #options = undetected_chromedriver.ChromeOptions()
    options = ec.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    #undetected_chromedriver.ChromeOptions()
    #options.add_argument('--proxy-type=socks5')
    #options.add_argument(f'--proxy-server={proxy}')
    #webdriver_options = {
    #    'proxy': {
    #        'address': '192.168.42.70:30002',  # Your proxy server address and port
    #        'use_proxy': True,
    #        'http_proxy': 'http://192.168.42.70:30002',  # HTTP Proxy config
    #        'https_proxy': 'https://192.168.42.70:30002',  #proxying, if needed
    #        'proxy_type': 'socks5',  # Specify the proxy ty# HTTPS Proxy config
    #        'no_proxy': '',  # Exclude specific URLs from pe (socks5, http, etc.)
    #    }
    #}
    #options = {
    #    'proxy': {
    #        'http': 'socks5://user:pass@192.168.10.100:8888',
    #        'https': 'socks5://user:pass@192.168.10.100:8888',
    #        'no_proxy': 'localhost,127.0.0.1'
    #    }
    #}
    #driver = webdriver.Chrome(seleniumwire_options=options)
    #options.add_argument(f'--proxy-server={proxy}')
    #options.add_argument('--disable-blink-features=AutomationControlled')
    #options.add_argument(
    #    '--user-agent=Mozilla/5.0 (Linux; Android 11; Pixel 4)\
    #    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36'
    #)
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(
        #seleniumwire_options=proxy_options,
        #seleniumwire_options=options,
        seleniumwire_options=options,
        service=service,
    )
    return driver


def register_user_account_in_it_wallapop(driver: webdriver.Chrome) -> None:
    try:
        driver.get(url="https://whoer.net/")
        sleep(30)
    except Exception as exception:
        logger.error(exception)
    finally:
        driver.close()
        driver.quit()


register_user_account_in_it_wallapop(
    create_driver(proxy='95.245.161.134:30000')
)
