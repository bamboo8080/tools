# Author：bamboo
# 大 道 至 简 ！

import time
import requests
# 超级ping
def sping(domain):
    params = {
        'format':'json',
        'ip':'{}'.format(domain),
    }
    try:
        response = requests.get('https://api.gmit.vip/Api/Sping', params=params)
        ping = dict(response.json())
        for k,v in ping['info']['request'].items():
            print('[+] ' + k + ': ' + v)
    except Exception:
        pass

sping('www.tit.edu.cn')