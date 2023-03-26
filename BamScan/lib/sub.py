# Author：bamboo
# 大 道 至 简 ！

import requests
import urllib3
from queue import Queue
import threading
urllib3.disable_warnings()





# 子域名
def sub(d,s):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
    }
    try:
        response = requests.head(f'https://{s}.{d}', headers=header, verify=False)
        if response.status_code < 404:
            print(f'[+] 存在子域名，subDomain: http://{s}.{d}')
    except requests.exceptions.ConnectionError:
            requests.status_codes = 'xxx'

# 多线程
def q_get(q,lock,d):
    while True:
        lock.acquire()
        s = q.get()
        sub(d,s)
        lock.release()
        if q.empty():
            break

# 主方法
def main(domain):
    print('[+] 子域名爆破')
    with open('./static/sub.txt','r') as f:
        # 生成队列
        q = Queue()
        for sub in f.read().split('\n'):
            q.put(sub)
        # 上锁
        lock = threading.Lock()
        for j in range(4):
            task = threading.Thread(target=q_get, args=(q, lock, domain))
            task.start()

if __name__ == '__main__':
    main('tit.edu.cn')
