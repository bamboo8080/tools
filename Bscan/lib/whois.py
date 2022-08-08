# Author：bamboo
# 大 道 至 简 ！

import requests
import re
# Whois
def main(domain):
    try:
        response = requests.get(f'https://v.api.aa1.cn/api/whois/index.php?domain={domain}')
        whois = re.findall('(.*: .*)',response.text)
        for i in whois:
            print('[+] ' + i)
    except Exception:
        pass
