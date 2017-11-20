# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.models import User

from qa.models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length=255, min_length=1)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        question = Question(**self.cleaned_data)
        question.author = User.objects.first()
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

    def __init__(self, question_id, *args, **kwargs):
        self._question_id = question_id
        super(AnswerForm, self).__init__(*args, **kwargs)


    def save(self):
        self.cleaned_data['question_id'] = self._question_id
        self.cleaned_data['author'] = User.objects.last()
        answer = Answer(**self.cleaned_data)
        answer.save()
