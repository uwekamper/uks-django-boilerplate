#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html', {})
