# bam_portScan

**工具版本：**v1.0

**简介：**portScan基于python编写，通过socket、click、thread、queue实现端口快速扫描。输入host，端口即可快速扫描，并输出有效端口信息到output.txt

**依赖安装**

```shell
pip install  -r requirements.txt  -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```

**使用方法：**

```python
python portScan.py --host 39.101.163.7 --port 1-1000

python portScan.py --host 39.101.163.7 --port 22,25,26
```

![image-20220607170723940](C:\Users\bamboo\AppData\Roaming\Typora\typora-user-images\image-20220607170723940.png)

![image-20220607170956282](C:\Users\bamboo\AppData\Roaming\Typora\typora-user-images\image-20220607170956282.png)

注：本工具仅用于测试，造成不良后果，与作者无关。