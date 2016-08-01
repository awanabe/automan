# coding=utf-8
__author__ = 'tech.chao'

import paramiko
# import select

try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('', 22, '', '')

    s_in, s_out, s_err = client.exec_command('cd /data/code/kkd && source ~/.virtualenvs/kkd/bin/activate && /data/bin/uwsgictl restart')
    print(s_out.read().decode('utf-8').split('\n'))
    print(s_err.read().decode('utf-8').split('\n'))

    #
    # channel = client.get_transport().open_session()
    # channel.exec_command('workon kkd')
    # channel.exec_command('pip install bs4')
    # while not channel.exit_status_ready():
    #     rl, wl, xl = select.select([channel], [], [], 0.0)
    #     if len(rl) > 0:
    #         print(channel.recv(1024))
    #
    # while channel.recv_stderr_ready():
    #     print(channel.recv_stderr(1024))
    #
    # channel.close()
except Exception as e:
    print(e)
