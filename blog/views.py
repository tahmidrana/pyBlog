# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'all_post':posts})

def single_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'blog/single.html', {'single_post':post})
