# Author：bamboo
# Time： 2022.06.09
# 介绍：信息搜集工具主函数
from util.banner import banner
from util import whois_info,port_info,dirpath_info,subdomain_info
from util.ICP_info import icp_api
from util.finger_info import finger

def main():
    banner()
    # onezyh.cn
    domain = input("请输入域名")
    print('------------------icp信息--------------------')
    icp_api(domain)
    print('------------------whois信息--------------------')
    whois_info.whois_api(domain)
    print('------------------指纹信息--------------------')
    ip = finger(domain)
    print('------------------路径爆破--------------------')
    dirpath_info.main('http://'+domain)
    print('------------------端口信息--------------------')
    port_info.main(ip)
    print('------------------子域名爆破--------------------')
    subdomain_info.main(domain)






if __name__ == '__main__':
    main()