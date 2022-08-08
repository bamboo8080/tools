# Author：bamboo
# 大 道 至 简 ！
import time

from lib import dir,icp,port,sub,whois


def Bscan():
    print('============================================欢迎使用AScan==============================================')
    print('''
    ########   ######   ######     ###    ##    ## 
    ##     ## ##    ## ##    ##   ## ##   ###   ## 
    ##     ## ##       ##        ##   ##  ####  ## 
    ########   ######  ##       ##     ## ## ## ## 
    ##     ##       ## ##       ######### ##  #### 
    ##     ## ##    ## ##    ## ##     ## ##   ### 
    ########   ######   ######  ##     ## ##    ##
          ''')
    print('=====================================================================================================')
    print('''
    扫描模块：
    1、Whois，ICP备案查询
    2、子域名爆破
    3、目录爆破
    4、端口扫描
    请选择对应的序号进行扫描
    ''')

    while True:
        t = input('请输入对应扫描模式序号：').strip()
        if t == '1':
            domian = input('请输入域名：')
            whois.main(domian)
            icp.main(domian)
            continue
        elif t == '2':
            domian = input('请输入域名：')
            sub.main(domian)
        elif t == '3':
            domian = input('请输入域名：')
            dir.main(domian)
        elif t == '4':
            ip = input('请输入IP：')
            port.main(ip)
            time.sleep(1)
        else:
            break

if __name__ == '__main__':
    Bscan()
