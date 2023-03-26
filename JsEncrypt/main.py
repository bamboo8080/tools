# Author：bamboo
# 大 道 至 简 ！
# 这是一个js加解密工具，只需要将js脚本放入当前目录即可。
import execjs
import os
from queue import Queue
import threading

# 加密函数
def js_encrypt(payload):
    path = os.listdir('./js/')
    with open("./js/%s" %path[0],'r',encoding='utf-8') as f:
        crypt = execjs.compile(f.read())
        payload = crypt.call(
            "encrypt",
            "%s" %payload)
        with open('./result/encrypt_payload.txt', 'a+', encoding='utf-8') as fi:
            fi.write("%s\n" %payload)



# 多线程加密函数
def encrypt_thread(q, lock):
    while True:
        lock.acquire()
        payload = q.get()
        js_encrypt(payload)
        lock.release()
        if q.empty():
            print('payload加密完成')
            break

with open('./result/payload.txt', 'r', encoding='utf-8') as f:
    # 生成队列
    q = Queue()
    for payload in f.read().split('\n'):
        q.put(payload)
    # 上锁
    lock = threading.Lock()
    for j in range(5):
        task = threading.Thread(target=encrypt_thread, args=(q, lock))
        task.start()