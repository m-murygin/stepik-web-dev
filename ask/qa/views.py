# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.http import require_GET
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from qa.models import Question


def test(request, *args, **kwargs):
    return HttpResponse('OK')

@require_GET
def question_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'qa/detail.html', {
        'question': question,
    })


@require_GET
def question_list(request, *args, **kwargs):
    questions_list = Question.objects.new()

    return show_questions_list(request, questions_list)


@require_GET
def popular(request, *args, **kwargs):
    questions_list = Question.objects.popular()

    return show_questions_list(request, questions_list)


def show_questions_list(request, queryset):
    paginator = Paginator(queryset, 10)

    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'qa/questions_list.html', {
        'questions': questions
    })

