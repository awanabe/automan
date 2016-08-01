# coding=utf-8
__author__ = 'tech.chao'

from . import OpDefine


class PipInstallOp(OpDefine):
    def __init__(self, path, prev_ops, req_txt_path):
        super().__init__(path, prev_ops)
        self.req_txt_path = req_txt_path
