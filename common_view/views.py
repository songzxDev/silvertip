# -*- coding: utf-8 -*-
# @Time    : 2018/11/6 0006 下午 9:24
# @Author  : songzxDev
# @Email   : songzx_2326@163.com
# @File    : views.py.py
# @Software: PyCharm
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
