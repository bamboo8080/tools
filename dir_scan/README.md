# bam_dirScan

**工具版本：**v1.0

**简介：**dirScan基于python编写，通过requests、click、thread、queue实现目录快速扫描。输入url 线程数即可快速扫描，并输出有效url到output.txt

**依赖安装**

```shell
pip install  -r requirements.txt  -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```

**使用方法：**

```python
python dirScan.py --url http://192.168.0.105 --thread 4
```

![image-20220607151111569](C:\Users\bamboo\AppData\Roaming\Typora\typora-user-images\image-20220607151111569.png)

注：本工具仅用于测试，造成不良后果，与作者无关。