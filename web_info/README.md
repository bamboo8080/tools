# bam_web_info

工具版本：1.0

简介：练手项目，基于接口对测试站点进行信息收集，包括whois、icp备案、指纹信息，端口信息、子域名爆破、路径爆破。

还在研究，可能会有报错，请谅解哈。

抛砖引玉。

花花世界迷人眼，大道至简！

**依赖安装**

```shell
pip install  -r requirements.txt  -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```

**使用方法：**

```python
需要去http://finger.tidesec.com/注册账号获取自己的cookie，放入util目录下finger文件的cookie位置
python main.py 
输入域名,例如 baidu.com 
```

![a](E:\PyProject\tools\web_info\a.png)