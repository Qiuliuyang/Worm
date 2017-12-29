#!/usr/bin/python
# _*_ coding: utf-8 _*_
# __author__ = "Qiu"
# Email = "qiu@immunet.cn"
import requests
#url = "https://www.amazon.cn/gp/product/B01M8L5z3Y"
kv = {'User-Agent':'Mozilla/5.0'}
kv2 = {'wd':'Python'}
try:
    r = requests.get("https://www.baidu.cn/s",params=kv2,headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print (r.text[:1000])
except:
    print (u"爬取失败")

print r.status_code
print r.request.headers
print r.request.url