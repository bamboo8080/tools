# Author：bamboo
# 大 道 至 简 ！
import re

import requests

def search(domain):
    params = {
        'q': 'inurl%3A%27{}%27'.format(domain),
    }
    try:
        response = requests.get('https://www.bing.com/search', params=params)
        print(response.text)
    except Exception:
        pass

def rapiddns(domain):
    try:
        response = requests.get('https://rapiddns.io/subdomain/{}?full=1&down=1#result'.format(domain))
        result = re.findall('<td>(.*).tit.edu.cn</td>', response.text)
        for i in result:
            print('[+] {0}.{1}'.format(i,domain))
    except Exception:
        pass
