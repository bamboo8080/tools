## 渗透测试工具集


- Bscan 信息收集工具
- poc扫洞

## 浅记--关于Clash的使用

### 一、安装

Clash 是由Dreamacro 开发的，是一个使用Go 开发的、基于规则的隧道，在中国大陆地区可用于突破防火长城的限制。 2020 年末，Dreamacro在GitHub仓库释出Clash的衍生版本Premium，而不提供其原始码。

[Clash for Windows](https://uzbox.com/tag/clash-for-windows) 是运行在 [Windows](https://uzbox.com/tag/windows) 上的一图形化 Clash 分支。通过 Clash API 来配置和控制 Clash 核心程序，便于用户可视化操作和使用。

Clash 是一个基于规则的跨平台代理软件核心程序。支持 SS / VMess 协议 。

Clash: https://github.com/Fndroid/clash_for_windows_pkg/releases

Clash汉化: https://github.com/BoyceLig/Clash_Chinese_Patch/releases

Proxy插件: https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif?hl=zh-CN

### 二、使用

#### 科学上网三模式：

- 直连模式：流量不经过节点，即不进行科学上网。
- 全局模式：所有流量经过节点，即全部软件都进行科学上网。
- PAC模式：PAC即规则文档，流向墙外的走节点通道，流向墙内的正常通道

#### 使用方式

请食用官方文档: https://docs.cfw.lbyczf.com/


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
