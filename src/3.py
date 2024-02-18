import time
from seleniumwire import undetected_chromedriver


def browser_with_proxy():
    """Браузер с прокси без авторизации в формате ip:port"""
    chrome_options=undetected_chromedriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')

    wire_options = {
        'proxy': {
            'https': 'socks5://95.245.161.134:30000/',
        }
    }
    driver = undetected_chromedriver.Chrome(seleniumwire_options=wire_options, options=chrome_options)
    #driver.uc()
    driver.get("https://2ip.ru")
    time.sleep(150)

browser_with_proxy()
