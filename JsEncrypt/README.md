# JsEncrypt

#### author：bamboo

#### 创作原因：

为了更快的对登录功能点进行暴力破解

#### 工具介绍：

这是一款 **多线程** **加密** 暴力破解payload的工具。



#### 环境：

```bash
pip install PyExecJS -i pip源
```

#### 使用方法·：

1. 将逆向出来的的JavaScript脚本放入js/目录下
2. JavaScript脚本的加密函数改为encrypt
3. 将需要加密的payload放入/result/payload.txt文件
4. 运行 main.py 即可