# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: 远程linux文件上传下载.py
# @ide: PyCharm
# @time: 2020/7/5 20:44
import paramiko

# 创建 ssh 对象
ssh = paramiko.SSHClient()
# 连接方式
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接远程机器(ip地址，端口号，远程主机已存在的用户名和密码)
ssh.connect("", 22, "songqin", "songqin")

sftp = ssh.open_sftp()

# 将本地文件上传到远程linux,第一个参数：本地文件路径；第二个参数：远程文件需要保存的路径
# sftp.put("", "/home/songqin/Desktop/test.py")

# 将远程Linux文件下载到本地,第一个参数：远程机器路径；第二个参数：本地保存文件路径
sftp.get("/home/songqin/Desktop/test.py","./a.py")

# 关闭ssh连接
ssh.close()