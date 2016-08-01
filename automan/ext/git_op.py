# coding=utf-8
__author__ = 'tech.chao'

from . import OpDefine


class GitOp(OpDefine):
    def __init__(self, path, prev_ops, branch):
        super().__init__(path, prev_ops)
        self.branch = branch

    def _gen_cmd_list(self):
        _cmds = ['cd %s' % self.path]
        if self.prev_ops:
            for _op in self.prev_ops: _cmds.append(_op)
        _cmds.append('git pull')
        _cmds.append('git checkout %s' % self.branch)
        self._cmds = _cmds
