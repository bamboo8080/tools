# Author：bamboo
# 大 道 至 简 ！

import requests
# whois
def whois(domain):
    params = {
        'format':'json',
        'domain':'{}'.format(domain),
    }
    try:

        response = requests.get('https://api.gmit.vip/Api/Whois', params=params)
        whois = dict(response.json())
        for k,v in whois['data'].items():
            print('[+] ' + k + ': ' + v)
    except Exception:
        pass
