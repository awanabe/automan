# coding=utf-8
__author__ = 'tech.chao'

import paramiko
import select


class OpDefine(object):
    def __init__(self, path, prev_ops):
        self.path = path or '~'
        self.prev_ops = prev_ops
        self._channel = None
        self._cmds = None

    def run(self, client):
        self._get_channel_by_client(client)
        try:
            self._gen_cmd_list()
            self._run()
        except Exception as e:
            print('[Op RUN ERROR] %s' % e)
        finally:
            self._channel.close()

    def _run(self):
        print('Run >> %s' % (' && '.join(self._cmds)))
        self._channel.exec_command(' && '.join(self._cmds))
        while not self._channel.exit_status_ready():
            print(self._channel.recv(1024).decode('utf8'))

        while self._channel.recv_stderr_ready():
            print(self._channel.recv_stderr(1024).decode('utf8'))

    def _get_channel_by_client(self, client):
        if not isinstance(client, paramiko.SSHClient):
            raise RuntimeError()

        self._channel = client.get_transport().open_session()

    def _gen_cmd_list(self):
        raise NotImplementedError()
