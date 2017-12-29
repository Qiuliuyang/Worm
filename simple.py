#!/usr/bin/python
# _*_ coding: utf-8 _*_
# __author__ = "Qiu"
# Email = "qiu@immunet.cn"
import requests
url = "https://www.jd.com/2017?t="
try:
    r = requests.get(url,timeout = 0.1)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print (r.text[:1000])
except:
    print (u"爬取失败")