# Author：bamboo
# Time：2022/6/21 16:14
# 大 道 至 简！

import requests

def finger(domain):
    try:
        cookies = {

        }
        data = {
            'target': domain,
        }
        response = requests.post('http://finger.tidesec.com/home/index/reget', cookies=cookies, data=data)
        response.encoding='utf-8'
        tide = dict(response.json()['res'])
        for k,v in tide.items():
            print('[+] ' + k + ': ' + str(v))
        return response.json()['res']['ip']
    except Exception:
        pass


