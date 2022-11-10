import requests
import base64
from config import config
import os
import zlib
import json
from core import basic
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import queue
from requests.packages import urllib3
import threading
'''
    此处存放三方接口，可直接调用，当前接口如下：
    whatweb              可直接调用whatweb接口进行指纹识别
    get_fofa_search_url  可直接调用获取所有的fofa搜索结果（未过滤）
    
'''

os.environ['NO_PROXY'] = 'fofa.info'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',}


def whatweb(url):
    '''
    调用whatweb接口对目标站点的CMS进行识别

    输入参数：
    'https://aliyun.bugscaner.com'
    返回结果：
    {'Web Servers': ['Tengine'], 'CDN': ['AliyunCdn'], 'url': 'aliyun.bugscaner.com'}

    '''
    response = requests.get(url,verify=False,timeout=2)
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    #上面的代码可以随意发挥,只要获取到response即可
    #下面的代码您无需改变，直接使用即可
    whatweb_dict = {"url":response.url,"text":response.text,"headers":dict(response.headers)}
    whatweb_dict = json.dumps(whatweb_dict)
    whatweb_dict = whatweb_dict.encode()
    whatweb_dict = zlib.compress(whatweb_dict)
    data = {"info":whatweb_dict}
    return requests.post("http://whatweb.bugscaner.com/api.go",files=data)

def get_fofa_search_url(fofa):
    '''
     获取fofa搜索url

     输入参数：
     title='apache'
     返回结果：
    ['i-sharing.pku.edu.cn', '162.105.209.62', '80'], ['https://115.27.240.21', '115.27.240.21', '443']
     '''
    result = []
    try:
        flag = base64.b64encode(fofa.encode()).decode()
        url = config.api.format(config.email, config.api_key, flag)
        response = requests.get(url)
        result = response.json()['results']
    except:
        print('请求fofa接口出现了问题')
    return result



if __name__ == '__main__':
    print(get_fofa_search_url("title='北京大学'"))