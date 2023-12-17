# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse


def index(request):
    context = {
        'segment': 'index',
    }

    return render(request, 'home/index.html', context)


def about(request):
    context = {
        'segment': 'about',
    }

    return render(request, 'home/page-about-us.html', context)


def error_404(request, exception):
    return render(request, 'home/404.html', status=404)