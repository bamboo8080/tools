## 渗透测试工具集


- Bamscan 信息收集工具
- pocNday扫洞
- TomcatScan 漏洞扫描工具





## 工具集

ARL资产灯塔系统：https://github.com/TophantTechnology/ARL

Clash（支持 SS / VMess 协议）: https://github.com/Fndroid/clash_for_windows_pkg/releases

Proxy插件: https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif?hl=zh-CN



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
