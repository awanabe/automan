# coding=utf-8
__author__ = 'tech.chao'

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('121.41.62.246', 22, 'root', 'ZGFpbHlzZXJ2aWNl', timeout=10)

std_in, std_out, std_err = ssh.exec_command('cd /data/code/kkd && git pull')
print(std_out.read())
if std_err.read():
    print('error occurs')
ssh.close()
