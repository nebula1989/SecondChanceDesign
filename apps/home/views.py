# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.conf import settings
import os



def index(request):

    # Path to your media folder
    
    media_folder_path = settings.MEDIA_ROOT
    images = []

    for root, dirs, files in os.walk(media_folder_path):
        for file in files:
            if file.lower().endswith(('jpg', 'jpeg', 'png', 'gif')):
                images.append(os.path.join(settings.MEDIA_URL, os.path.relpath(os.path.join(root, file), media_folder_path)))

    context = {
        'segment': 'index',
        'images': images
    }

    return render(request, 'home/index.html', context)


def about(request):
    context = {
        'segment': 'about',
    }

    return render(request, 'home/page-about-us.html', context)


def error_404(request, exception):
    return render(request, 'home/404.html', status=404)