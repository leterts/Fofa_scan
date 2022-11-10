import requests
import base64
from config import config
from core import extend_interface
import os

def get_all_title():
    ''' 获取文件中所有目标的title '''
    filepath = os.getcwd()
    filepath = filepath + os.path.sep + 'file' + os.path.sep + 'target.txt'
    L = []
    with open(filepath, 'r', encoding='UTF-8') as f:
        for i in f.readlines():
            L.append(i.strip())
    return L

# 进行搜索结果存储
def save(fofasearch_result,file):
    '''获取result文件的路径'''
    path = os.getcwd()
    '''适配windows系统及linux系统'''
    if os.name == 'nt':
        path = path + '\\result\\'
    if os.name == 'posix':
        path = path + '/result/'

    if os.path.exists(path):
        path = path + file
        with open(path,'w') as f:
            for i in fofasearch_result:
                f.write(i+'\n')


def get_fofa_result():
    '''获取fofa搜索结果'''
    L = []
    for i in get_all_title():
        for k in extend_interface.get_fofa_search_url(i):
            L.append(k)
    return L

