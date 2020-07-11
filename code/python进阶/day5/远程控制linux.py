# -*- coding: utf-8 -*-
# @project : code
# @author: Administrator
# @file: 远程控制linux.py
# @ide: PyCharm
# @time: 2020/7/5 20:12
import paramiko

# 创建 ssh 对象
ssh = paramiko.SSHClient()
# 连接方式
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接远程机器(ip地址，端口号，远程主机已存在的用户名和密码)
ssh.connect("", 22, "songqin", "songqin")
# 执行命令
stdin, stdout, stderr = ssh.exec_command("ls")
print(stdout.read().decode("utf8"))

stdin, stdout, stderr = ssh.exec_command("cd Desktop;pwd")
print(stdout.read().decode("utf8"))

# 再次执行命令 ：相当于打开一个新的终端
stdin, stdout, stderr = ssh.exec_command("pwd")
print(stdout.read().decode("utf8"))

# 关闭ssh连接
ssh.close()