# coding=utf-8
__author__ = 'tech.chao'

from . import OpDefine

class UWSGIRestartOp(OpDefine):
    def __init__(self, path, prev_ops, cmd):
        super().__init__(path, prev_ops)
        self.cmd = cmd

    def _gen_cmd_list(self):
        _cmds = ['cd %s' % self.path]
        if self.prev_ops:
            for _op in self.prev_ops: _cmds.append(_op)
        _cmds.append(self.cmd)
        self._cmds = _cmds