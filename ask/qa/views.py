# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.views.decorators.http import require_GET
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate


from qa.models import Question
from qa.forms import AskForm, AnswerForm, SignupForm


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()

    return render(request, 'registration/signup.html', { 'form': form })


def ask_view(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

        form = AskForm(request.user, request.POST)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect(question.get_url())
    else:
        form = AskForm(request.user)

    return render(request, 'qa/ask.html', {'form': form})


def question_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answers = question.answer_set.all()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        form = AnswerForm(question, request.user, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    else:
        form = AnswerForm(question, request.user)

    return render(request, 'qa/detail.html', {
        'form': form,
        'question': question,
        'answers': answers,
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
