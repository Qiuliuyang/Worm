#!/usr/bin/python
# _*_ coding: utf-8 _*_
# __author__ = "Qiu"
# Email = "qiu@immunet.cn"
import os
import requests
kv = {'User-Agent':'Mozilla/5.0'}
url1 = "https://images-cn.ssl-images-amazon.com/images/I/41C9U6RDdSL._SX340_BO1,204,203,200_.jpg"
d ="/Users/pro/Desktop/pic/"
dt = d + url1.split('/')[-1]
try:
    if not os.path.exists(d):
        os.mkdir(d)
    if not os.path.exists(dt):
        r = requests.get(url1,headers = kv)
        r.raise_for_status()
        with open(dt,'wb') as pic:
            pic.write(r.content)
            pic.close()
            print (u'文件保存成功')
    else:
        print (u'文件已存在！请勿重复爬取')
except:
    print (u"爬取失败")

print r.status_code
print r.request.headers
print r.request.url