# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from models import Question


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def question_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'qa/detail.html', {
        'question': question,
    })


def question_list(request, *args, **kwargs):
    return HttpResponse('OK_list')


def popular(request, *args, **kwargs):
    return HttpResponse('OK_popular')
