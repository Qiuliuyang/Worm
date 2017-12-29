#!/usr/bin/python
# _*_ coding: utf-8 _*_
# __author__ = "Qiu"
# Email = "qiu@immunet.cn"
import requests
url = "https://www.amazon.cn/gp/product/B01M8L5z3Y"
kv = {'User-Agent':'Mozilla/5.0'}
try:
    r = requests.get(url,headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print (r.text[:1000])
except:
    print (u"爬取失败")

print r.status_code
print r.request.headers