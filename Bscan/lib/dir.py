# Author：bamboo
# 大 道 至 简 ！

import requests
import urllib3
from queue import Queue
import threading
urllib3.disable_warnings()




# 目录爆破
def dir(d,r):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
    }
    try:
        response = requests.get(f'https://{d}/{r}', headers=header, verify=False)
        if response.status_code == 200:
            print(f'[+] Domain: https://{d}/{r}, 状态码: {response.status_code}')
    except Exception as e:
        pass

# 多线程
def q_get(q,lock,d):
    while True:
        lock.acquire()
        r = q.get()
        lock.release()
        dir(d,r)
        if q.empty():
            break

# 主函数
def main(d):
    print('======================================================')
    print('目录路径爆破')
    print('======================================================')
    with open('./static/dir.txt','r') as f:
        # 生成队列
        q = Queue()
        for r in f.read().split('\n'):
            q.put(r)
        # 上锁
        lock = threading.Lock()
        for j in range(5):
            task = threading.Thread(target=q_get, args=(q, lock, d))
            task.start()

# if __name__ == '__main__':
#     main('jizhicms.ledevcloud.cn')