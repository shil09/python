#!/usr/bin/env python3
import requests

#从指定的URL中下载文件的程序
def download(url):
    '''
    从指定的URL中下载文件并存储到当前目录
    url: 要下载页面内容的网址
    '''
    try:
        req = requests.get(url)
    except requests.exceptions.MissingSchema:
        print('Invalid URL"{}"'.format(url))
        return
#检查是否成工访问了该网站
    if req.status_code == 403:
        print('没有权限访问该网站')
        return
    filename = url.split('/')[-1]
    with open(filename,'w') as fobj:
        fobj.write(req.content.decode('utf-8'))
    print("Download over.")

if __name__ == '__main__':
    url = input("请输入一个url:")
    download(url)

