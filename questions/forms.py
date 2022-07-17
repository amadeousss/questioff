from django import forms
from .models import Question, Answer
from django.core.validators import MaxLengthValidator


class QuestionForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Type your question', 'maxlength': '250'}),
                              validators=[MaxLengthValidator(250)])

    class Meta:
        model = Question
        fields = ('content',)


class AnswerForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Type your question', 'maxlength': '250'}),
                              validators=[MaxLengthValidator(200)])

    class Meta:
        model = Answer
        fields = ('content',)
