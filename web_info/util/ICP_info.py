# Author：bamboo
# Time：2022/6/21 10:34
# 大 道 至 简！

import requests

def icp_api(domain):
    try:
        response = requests.get(f'https://v.api.aa1.cn/api/icp/index.php?url={domain}')
        icp = dict(response.json())
        for k,v in icp.items():
            print('[+]  ' + k + ': ' + v)
    except Exception:
        pass



