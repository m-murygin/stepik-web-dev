# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.models import User

from qa.models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length=255, min_length=1)
    text = forms.CharField(widget=forms.Textarea)

    def __init__(self, user, *args, **kwargs):
        super(AskForm, self).__init__(*args, **kwargs)
        self._user = user

    def save(self):
        question = Question(**self.cleaned_data)
        question.author = self._user
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def __init__(self, question, user, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.fields['question'].initial = question.id
        self._user = user


    def save(self):
        question = Question.objects.get(pk=self.cleaned_data['question'])
        self.cleaned_data['question'] = question
        self.cleaned_data['author'] = self._user
        answer = Answer(**self.cleaned_data)
        answer.save()


class SignupForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)

    def save(self):
        User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password')
        )
