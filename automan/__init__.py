# coding=utf-8
__author__ = 'tech.chao'

from flask import Flask

import config

app = Flask(__name__)
app.debug = config.DEBUG_MODE


@app.route('/', methods=['GET'])
def index():
    return 'This is Index'

