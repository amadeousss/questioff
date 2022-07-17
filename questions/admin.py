from django.contrib import admin
from .models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('content', 'asked_user', 'created_at')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('content', 'question', 'asked_user', 'created_at')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
