# coding=utf-8
__author__ = 'tech.chao'


class OpDefine(object):
    def __init__(self, path, prev_ops):
        self.path = path or '~'
        self.prev_ops = prev_ops


#
# def load_config(self, _config):
#     raise NotImplementedError()


class GitOp(OpDefine):
    def __init__(self, path, prev_ops, branch):
        super().__init__(path, prev_ops)
        self.branch = branch


class PipUpdateOp(OpDefine):
    def __init__(self, path, prev_ops, req_txt_path):
        super().__init__(path, prev_ops)
        self.req_txt_path = req_txt_path


class MigrateUpdateOp(OpDefine):
    def __init__(self, path, prev_ops, migrate_main_file):
        super().__init__(path, prev_ops)
        self.migrate_main_file = migrate_main_file


class UWSGIRestartOp(OpDefine):
    def __init__(self, path, prev_ops, cmd, ini_file):
        super().__init__(path, prev_ops)
