# Author：bamboo
# 大 道 至 简 ！

import requests
# ICP
def icp(domain):
    params = {
        'format':'json',
        'domain':'{}'.format(domain),
    }
    try:
        response = requests.get('https://api.gmit.vip/Api/ICP', params=params)
        icp = dict(response.json())
        for k,v in icp['data'].items():
            print('[+] ' + k + ': ' + v)
    except Exception:
        pass