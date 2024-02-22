
import requests
import sys

a = 'http://local.adspower.net:50325/api/v1/browser/start?user_id=jec5532'
host = '192.168.42.70'
port = '30001'
"""
group = 'testgroup'
create_group = requests.post(
    'http://local.adspower.net:50325/api/v1/group/create',
    json={'group_name': group}
).json()
print(create_group)
"""
"""
create = requests.post(
    'http://local.adspower.net:50325/api/v1/user/create', 
    json={
        'group_id': 3662521,
        'user_proxy_config': {
            'proxy_soft': '922S5',
            'proxy_type': 'socks5',
            'proxy_host': host,
            'proxy_port': port,
        },
        'country': 'it',
    },
).json()
if create:
    print(create)
    sys.exit()
"""
create = requests.get(
    'http://local.adspower.net:50325/api/v1/user/list', 
).json()
print(create)

#{"ua_browser":["chrome"],"ua_version":["80"],"ua_system_version":["Windows 10"]}
{'data': 
 {'list': 
  [
      {'name': '', 'domain_name': '', 'created_time': '1708376366', 'ip': '87.6.29.120', 
       'ip_country': 'it', 
       'password': '', 
       'fbcc_proxy_acc_id': '0', 'ipchecker': 'ip2location'
       #получить  бинд ип и кайф
########################################################################################
import socket
import requests,time
from selenium.webdriver.chrome.options import Options
import sys
from time import sleep
from random import choice

from loguru import logger
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from seleniumwire import undetected_chromedriver, webdriver

def get_my_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

my_ip = get_my_ip()
print("Your IP address is:", my_ip)

ads_id = "jed4x6k"
open_url = "http://local.adspower.net:50325/api/v1/browser/start?user_id=" + ads_id
close_url = "http://local.adspower.net:50325/api/v1/browser/stop?user_id=" + ads_id

resp = requests.get(open_url).json()
if resp["code"] != 0:
    print(resp["msg"])
    print("please check ads_id")
    sys.exit()

chrome_driver = resp["data"]["webdriver"]
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://its.wallapop.com/')
time.sleep(5)
driver.quit()
requests.get(close_url)


options = undetected_chromedriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors')

service = Service(executable_path=ChromeDriverManager().install())
driver = undetected_chromedriver.Chrome(
    seleniumwire_options=seleniumwire_options,
    service=service,
    options=options,
)
open_url = f'http://local.adspower.net:50325/api/v1/browser/start?user_id={profile_id}'
    #close_url = "http://local.adspower.net:50325/api/v1/browser/stop?user_id=" + ads_id

resp = requests.get(open_url).json()
if resp["code"] != 0:
    print(resp["msg"])
    print("please check ads_id")
    sys.exit()

chrome_driver = resp["data"]["webdriver"]
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://it.wallapop.com/')
return driver
####################################################################################################################

import requests,time
#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
import sys
#from seleniumwire import webdriver#undetected_chromedriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

open_url = "http://local.adspower.net:50325/api/v1/browser/start?user_id=jed4x6k" 
close_url = "http://local.adspower.net:50325/api/v1/browser/stop?user_id=jed4x6k" 

#resp = requests.get(open_url).json()
#if resp["code"] != 0:
#    print(resp["msg"])
 #   print("please check ads_id")
 #   sys.exit()

#chrome_driver = resp["data"]["webdriver"]
#chrome_options = Options()
#chrome_options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
#driver = webdriver.Chrome(options=chrome_options)

#service = Service(executable_path='c:\Users\berch\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
#service = Service(executable_path='c:/Users/berch/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')``
resp = requests.get(open_url).json()
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
#driver = undetected_chromedriver.Chrome(
chrome_driver = resp["data"]["webdriver"]
service = Service(chrome_driver)
#print(chrome_driver)
print(service)
driver = webdriver.Chrome(
    #seleniumwire_options=options,#None,
    #service=r(str(resp["data"]["webdriver"])),
    service=service,
    #service=service,
    options=options,
)
driver.get(url='https://intoli.com/blog/making-chrome-headless-undetectable/')
time.sleep(10)
#driver.quit()
#requests.get(close_url)
###########################################################################################################
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

open_url = "http://local.adspower.net:50325/api/v1/browser/start?user_id=jedbu3b" 
close_url = "http://local.adspower.net:50325/api/v1/browser/stop?user_id=jedbu3b" 

resp = requests.get(open_url).json()
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])

chrome_driver = resp["data"]["webdriver"]
service = Service(executable_path=chrome_driver)

driver = webdriver.Chrome(service=service, options=options)
driver.get('https://intoli.com/blog/making-chrome-headless-undetectable/')
time.sleep(10)
#####################################################################################################################

import requests,time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys

ads_id = "jedbu34"
open_url = "http://local.adspower.net:50325/api/v1/browser/start?user_id=" + ads_id
close_url = "http://local.adspower.net:50325/api/v1/browser/stop?user_id=" + ads_id

resp = requests.get(open_url).json()
if resp["code"] != 0:
    print(resp["msg"])
    print("please check ads_id")
    sys.exit()

chrome_driver = resp["data"]["webdriver"]
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
print(driver.title)
driver.get("https://www.baidu.com")
time.sleep(5)
driver.quit()
requests.get(close_url)
                  
#############################################################################################################################

import requests,time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random 
import string
from selenium.webdriver.chrome.service import Service
import sys

ads_id = "jeejwpf"
open_url = "http://local.adspower.net:50325/api/v1/browser/start?user_id=" + ads_id
close_url = "http://local.adspower.net:50325/api/v1/browser/stop?user_id=" + ads_id
resp = requests.get(open_url).json()
if resp["code"] != 0:
    sys.exit()
print(resp)
chrome_driver = resp["data"]["webdriver"]
service = Service(chrome_driver)
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
driver = webdriver.Chrome(service=service, options=chrome_options)
print(driver.title)
driver.get("https://www.baidu.com")
time.sleep(5)
driver.quit()
requests.get(close_url)
