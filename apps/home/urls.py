# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.urls import path

from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),


]
