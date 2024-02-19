
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
