#!usr/bin/env python
#---*---coding:utf-8---*---#
from django.http import HttpResponse

__author__ = 'Bruce.张'

def index_view(request):
    return HttpResponse('shangchuanchenggong ')