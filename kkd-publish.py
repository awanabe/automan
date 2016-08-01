# coding=utf-8
__author__ = 'tech.chao'

import config
from automan.ext.git_op import GitOp
from automan.ext.migrate_op import MigrateUpdateOp
from automan.ext.uwsgi_op import UWSGIRestartOp
from automan.process.core import Process

kkd_deploy_process = Process(
    host=config.KKD_HOST,
    port=config.KKD_PORT,
    username=config.KKD_USERNAME,
    password=config.KKD_PASSWORD,
    steps=[
        GitOp(
            path='/data/code/kkd',
            prev_ops=None,
            branch='master'
        ),
        MigrateUpdateOp(
            path='/data/code/kkd',
            prev_ops=['source ~/.virtualenvs/kkd/bin/activate'],
            migrate_main_file='migrate.py'
        ),
        UWSGIRestartOp(
            path='/data/code/kkd',
            prev_ops=['source ~/.virtualenvs/kkd/bin/activate'],
            cmd='/data/bin/uwsgictl restart'
        )
    ]
)

kkd_deploy_process.run()