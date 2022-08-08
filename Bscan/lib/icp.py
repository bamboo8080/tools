# Author：bamboo
# 大 道 至 简 ！

import requests
# ICP
def main(domain):
    try:
        response = requests.get(f'https://v.api.aa1.cn/api/icp/index.php?url={domain}')
        icp = dict(response.json())
        for k,v in icp.items():
            print('[+] ' + k + ': ' + v)
    except Exception:
        pass
