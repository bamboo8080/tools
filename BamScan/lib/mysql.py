import pymysql
import threading
def mysqlScan(t, i, u, p):
    try:
        t.acquire()
        db = pymysql.connect(host=i, user=u, password=p)
        print('[+]MYSQL连接成功，用户：%s,密码：%s' % (u, p))
        db.close()
    except:
        t.release()

def mysql(ip):
    with open('./static/username.txt', 'r')as f:
        user = f.readlines()
    with open('./static/password.txt', 'r')as f:
        passw = f.readlines()
    # ip = input("请输入IP：").strip()
    s = threading.Semaphore(10)
    for i in user:
        username = i.strip()
        for j in passw:
            password = j.strip()
            t = threading.Thread(target=mysqlScan, args=(s, ip, username, password))
            t.start()