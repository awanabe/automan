# coding=utf-8
__author__ = 'tech.chao'

import paramiko

from automan.ext import OpDefine


class Process(object):
    def __init__(self, host, port, username, password, steps):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.steps = steps

    def load_config(self, config_path):
        pass

    def run(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(self.host, self.port, self.username, self.password)

        for _step_op in self.steps:
            if not isinstance(_step_op, OpDefine):
                raise RuntimeError('StepOp is not an instance of OpDefine')
            _step_op.run(client)

        client.close()


