# Author：bamboo
# 大 道 至 简 ！

import requests
import base64
def fofa(domain):
    params = {
        'email': '202054321@tit.edu.cn',
        'key': '填写您的key',
        'qbase64': '{}'.format(str(base64.b64encode(domain.encode("utf-8")), "utf-8"))
    }
    try:
        response = requests.get('https://fofa.info/api/v1/search/all', params=params)
        result = dict(response.json())
        print(result)
        for k, v in result['data'].items():
            print('[+] ' + k + ': ' + v)
    except Exception:
        pass
