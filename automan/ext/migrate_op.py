# coding=utf-8
__author__ = 'tech.chao'

from . import OpDefine


class MigrateUpdateOp(OpDefine):
    def __init__(self, path, prev_ops, migrate_main_file):
        super().__init__(path, prev_ops)
        self.migrate_main_file = migrate_main_file

    def _gen_cmd_list(self):
        _cmds = ['cd %s' % self.path]
        if self.prev_ops:
            for _op in self.prev_ops: _cmds.append(_op)
        _cmds.append('python %s db upgrade' % self.migrate_main_file)
        self._cmds = _cmds
