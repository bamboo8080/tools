# Author：bamboo
# Time：2022/6/17 11:17
# 大 道 至 简！

# import execjs
import re

import requests

# 旧whois api接口 响应迟钝。
# def whois_api(domain):
#     api = f"https://api.devopsclub.cn/api/whoisquery?domain={domain}&type=json&standard=true"
#     # api = f'https://v.api.aa1.cn/api/whois/index.php?domain={domain}'
#     response = requests.get(api)
#     # whois = response.json()['data']['data']
#
#     try:
#         # print(
#         #     '[*] '+"域名：" + whois['domainName'],
#         #     '[*] '+"注册人：" + whois['registrant'],
#         #     '[*] '+"注册商：" + whois['registrar'],
#         #     '[*] '+"域名状态：" + whois['domainStatus'],
#         #     '[*] '+"联系邮箱：" + whois['contactEmail'],
#         #     '[*] '+"联系电话：" + whois['contactPhone'],
#         #     '[*] '+"注册时间：" + whois['registrationTime'],
#         #     '[*] '+"更新时间：" + whois['updatedDate'],
#         #     # "DNS服务器：" + whois['dnsNameServer'][:],
#         #     sep='\n',
#         # )
#         print(response.text)
#
#     except Exception :
#         print("whois查询出现错误")
# 利用站长之家 页面 直接爬取
# def whois_zj(domain):
#     headers = {
#         'origin': 'https://whois.chinaz.com',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
#         'x-requested-with': 'XMLHttpRequest',
#     }
#     with open('../stitic/whois_token.js') as f:
#         js = execjs.compile(f.read())
#         token = js.call(
#             'get_token',
#             domain
#         )
#     data = {
#         'host': domain,
#         'isUp': 'False',
#         'ws': '',
#         'token': token,
#     }
#     response = requests.post('https://whois.chinaz.com/getWhoisInfo.ashx', headers=headers, data=data)
#     print(response.json())


def whois_api(domain):

    response = requests.get(f'https://v.api.aa1.cn/api/whois/index.php?domain={domain}')
    whois = re.findall('(.*: .*)',response.text)
    for i in whois:
        print('[+] ' + i)

