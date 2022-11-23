# from django.forms import forms
from django import forms
from . import models


class QuizForm(forms.ModelForm):
    class Meta:
        model = models.Quizs
        fields = ('qus', 'op1', 'op2', 'op3', 'op4', 'ans')
