# Author: bamboo
# Time: 2022.06.07
# 简介：目录扫描脚本v1.0
import requests
from queue import Queue
import threading



# 载入字典
def dirs():
    with open('./stitic/dir.txt', 'r') as f:
        dirs = f.read().split('\n')
    return dirs

# 路径扫描
def dir_scan(url,dir):
    target = url + dir
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
    }
    # proxies = {
    #     "http":"http://127.0.0.1:8080"
    # }

    response = requests.get(target, headers=header)
    if response.status_code  < 400:
        print("[+] " + target + " ,状态码：" + str(response.status_code))
# 多线程
def q_get(q,lock,url):
    while True:
        lock.acquire()
        dir = q.get()
        lock.release()
        url = url
        dir_scan(url, dir)
        if q.empty():
            break

# 目录扫描主方法
def main(url):
    # 生成队列
    q = Queue()
    for dir in dirs():
        q.put(dir)
    # 上锁
    lock = threading.Lock()
    for j in range(5):
        task = threading.Thread(target=q_get, args=(q, lock, url))
        task.start()


