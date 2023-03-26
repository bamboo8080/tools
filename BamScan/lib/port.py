# Author：bamboo
# 大 道 至 简 ！

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
            print("[+] 端口: {}, 返回内容: {}".format(port,result))
        else:
            return False
    except Exception as e:
        pass
    finally:
        sk.close()

# 多线程
def q_get(ip,q,lock):
    while True:
        lock.acquire()
        p = q.get()
        connect(ip, p)
        lock.release()
        

        if q.empty():
            break

# 主方法
def main(ip):
    # 扫描端口列表
    ports_list = ['21', '22', '23', '25', '53', '81', '110', '139', '389', '445', '873', '1080', '1352', '1433', '1521'
                  ,'2049', '2181', '2375', '3306', '3389', '4440', '4848', '5000', '5432', '5632', '5900', '6082', '6379'
                  , '8000', '8009', '8080', '8082', '8089', '8181', '8649', '9000', '9090', '11211', '50000', '67', '68'
                  , '80', '443', '161', '162', '512', '513', '514', '7001', '7002', '8083', '8086', '9200', '9300', '8069'
                  , '10050', '27017', '27018', '28017', '8088', '50070', '50060']
    # 将端口放入队列
    q = Queue()
    for p in ports_list:
        q.put(p)
    # 上锁
    lock = threading.Lock()
    for j in range(4):
        task = threading.Thread(target=q_get, args=(ip, q, lock))
        task.start()
