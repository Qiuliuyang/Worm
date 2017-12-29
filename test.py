#!/usr/bin/python
# _*_ coding: utf-8 _*_
# __author__ = "Qiu"
# Email = "qiu@immunet.cn"
import requests
r = requests.get("http://www.baidu.com")
print r.status_code
r.encoding = 'utf-8'
