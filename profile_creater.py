import socket
import string
from random import choice
from time import sleep

import requests
import socks


def check_proxy(proxy_host, proxy_port):
    original_socket = socket.socket
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
    finally:
        socks.set_default_proxy()
        socket.socket = original_socket


def filter_proxies(proxy_list):
    filtered_proxies = []
    for proxy in proxy_list:
        proxy_host, proxy_port = proxy.split(':')
        if check_proxy(proxy_host, proxy_port):
            filtered_proxies.append(proxy)
        sleep(0.25)
    return filtered_proxies


def create_ads_power_group() -> str:
    group_name = ''.join(
        choice(string.ascii_letters + string.digits) for _ in range(8)
    )
    create_group = requests.post(
        'http://local.adspower.net:50325/api/v1/group/create',
        json={
            'group_name': group_name,
        },
    ).json()
    group_id = create_group['data']['group_id']
    print(f"Создана группа с названием {group_name}")
    return str(group_id)


def create_ads_power_profile(host, port, group_id) -> str | None:
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
                'ua_system_version': ['Android'],
            },
        },
    ).json()
    try:
        return create['data']['id']
    except Exception:
        print(create['msg'])
        return None


def create_proxy_list() -> list[str] | None:
    try:
        with open('proxy.txt', 'r') as f:
            proxie_choice = f.read().splitlines()
            return proxie_choice
    except Exception:
        return None


def get_random_unused_proxy(proxy_list: list) -> str:
    if proxy_list:
        random_proxy = choice(proxy_list)
        proxy_list.remove(random_proxy)
        return random_proxy
    else:
        return None


credentials_dict = int(input('Введите количество профилей которое необходимо зарегистрировать:'))
proxy_list = filter_proxies(create_proxy_list())
profile_ids = []
group_id = create_ads_power_group()

if len(proxy_list) >= credentials_dict:
    for i in range(credentials_dict):
        proxy_host, proxy_port = get_random_unused_proxy(proxy_list=proxy_list).split(':')
        profile_id = create_ads_power_profile(
            host=proxy_host,
            port=proxy_port,
            group_id=group_id,
        )
        if profile_id:
            profile_ids.append(profile_id)
        sleep(0.25)
    print(f'Количество созданных профилей: {len(profile_ids)}')
else:
    print('Количество рабочих прокси меньше необходимого')
    print(f'Количество рабочих прокси: {len(proxy_list)}')

sleep(15)
