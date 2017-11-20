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
    question = forms.IntegerField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        question = None
        if 'question' in kwargs:
            question = kwargs.pop('question')

        super(AnswerForm, self).__init__(*args, **kwargs)
        if question:
            self.fields['question'].initial = question


    def save(self):
        question = Question.objects.get(pk=self.cleaned_data['question'])
        self.cleaned_data['question'] = question
        self.cleaned_data['author'] = User.objects.last()
        answer = Answer(**self.cleaned_data)
        answer.save()
