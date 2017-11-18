# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def question(request, *args, **kwargs):
    return HttpResponse('OK_question')


def question_list(request, *args, **kwargs):
    return HttpResponse('OK_list')


def popular(request, *args, **kwargs):
    return HttpResponse('OK_popular')
