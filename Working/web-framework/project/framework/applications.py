'''
Web Framework
'''
from . import config
from . import utils

def index():
    return utils.get("index.html")

def center():
    return utils.get("center.html")

def application(env, start_response):
    '''
    Implementing interface of WSGI Protocol
    :param env:
    :param start_response:
    :return: html
    '''
    file_name = env['PATH_INFO']
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])

    if file_name == "/index.py":
        return index()
    elif file_name == "/center.py":
        return center()
    else:
        return '404'


