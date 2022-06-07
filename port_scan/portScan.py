# Author: bamboo
# Time: 2022.04.10
# 简介: 端口扫描v1.0
from socket import *
import threading
from queue import Queue
import click

def banner():
    portScanLog = '''
                                                     mmmm                                 
                                 ##                m#""""#                                
 ##m###m    m####m    ##m####  #######             ##m        m#####m   m#####m  ##m####m 
 ##"  "##  ##"  "##   ##"        ##                 "####m   ##"    "   " mmm##  ##"   ## 
 ##    ##  ##    ##   ##         ##                     "##  ##        m##"""##  ##    ## 
 ###mm##"  "##mm##"   ##         ##mmm             #mmmmm#"  "##mmmm#  ##mmm###  ##    ## 
 ## """      """"     ""          """"              """""      """""    """" ""  ""    "" 
 ##                                                                                       
                                        """"""""""  
    '''
    return print(portScanLog)
# 扫描端口
def connect(ip, port):
    try:
        sk = socket(AF_INET, SOCK_STREAM)
        sk.connect((ip, int(port)))
        sk.settimeout(3)
        result = sk.recv(1024)
        if result:
            port_info = "端口:{},返回内容:{}".format(port,result)
            print(port_info)
            with open('./output.txt', 'a+') as f:
                f.write(port_info + '\n')
        else:
            return False
    except Exception as e:
        pass
    finally:
        sk.close()
# 格式化端口
def get_ports(ports_dict):
    ports_list = []
    for port in ports_dict.split(","):
        if "-" in str(port):
            start_end = port.split('-')
            for i in range(int(start_end[0]), int(start_end[1])):
                ports_list.append(str(i))
        else:
            ports_list.append(port)

    return ports_list

def q_get(host,q,lock):
    while True:
        lock.acquire()
        port = q.get()
        lock.release()
        connect(host, port)

        if q.empty():
            break

@click.command()
@click.option('--host', help='输入目标ip.')
@click.option('--port', help='输入目标端口')
def main(host,port):
    banner()
    # 格式化端口
    ports_list = get_ports(port)
    # 将端口放入队列
    q = Queue()
    for i in ports_list:
        q.put(i)
    # 上锁
    lock = threading.Lock()
    for j in range(100):
        task = threading.Thread(target=q_get, args=(host, q, lock))
        task.start()

if __name__ == '__main__':
    main()