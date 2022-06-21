# Author: bamboo
# Time: 2022.04.10


from socket import *
import threading
from queue import Queue

# 扫描端口
def connect(ip, port):
    try:
        sk = socket(AF_INET, SOCK_STREAM)
        sk.connect((ip, int(port)))
        sk.settimeout(3)
        result = sk.recv(1024)
        if result:
            print('[+] '+ "端口:{},返回内容:{}".format(port,result))
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
# 多线程
def q_get(host,q,lock):
    while True:
        lock.acquire()
        port = q.get()
        lock.release()
        connect(host, port)

        if q.empty():
            break

# 端口扫描主方法
def main(host,port='21,22,80,443,445,3306,6379,8080,7001'):
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

