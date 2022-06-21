# Author：bamboo
# Time：2022/6/18 11:35
# 大 道 至 简！
# from fake_useragent import UserAgent
import time
import requests

# 子域名爆破
def domain_info(domain):
    url = 'http://' + domain
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            print("[+] 存在子域名：{}".format(url)+"状态码：{}".format(response.status_code))
    except Exception:
        pass
    except requests.exceptions.ConnectionError:
        response.status_code = "Connection refused"
    time.sleep(2)
# 子域名字典
def domian_dict(domain):
    # 空集合接收 域名 来达到去重目的
    subs = set()
    with open('./stitic/subdomain.txt','r') as f:
        for sub in f.read().split('\n'):
            url = sub + '.' + domain
            subs.add(url)
    return subs

def main(domain):
    for i in domian_dict(domain):
        domain_info(i)

