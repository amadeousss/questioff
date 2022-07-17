import datetime

from django.db import models
from users.models import CustomUser
from django.db.models import F


class Question(models.Model):
    content = models.CharField(max_length=250)
    asked_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # @property
    # def formatted_created_at(self):
    #     if self.created_at.year < datetime.datetime.now().year:
    #         return f"{self.created_at.date()}, {self.created_at.year}"
    #     else:
    #         # if (datetime.datetime.now(datetime.timezone.utc) - self.created_at).total_seconds() >= 86400*2:
    #         return f"{self.created_at.astimezone(datetime.timezone.utc).strftime('%H:%M, %b %d')}"
    #         # elif (datetime.datetime.now(datetime.timezone.utc) - self.created_at).total_seconds() >= 86400:
    #         #     return f"Yesterday, {str(100+self.created_at.hour)[1:3]}:{str(100+self.created_at.minute)[1:3]}"
    #         # else:
    #         #     return f"Today, {str(100+self.created_at.hour)[1:3]}:{str(100+self.created_at.minute)[1:3]}"

    class Meta:
        # ordering = ['answer', '-answer__created_at', '-created_at']
        ordering = [F('answer__created_at').desc(nulls_first=True), '-created_at']

    def __str__(self):
        return ' '.join(self.content.split(" ")[:10])


class Answer(models.Model):
    content = models.CharField(max_length=250)
    question = models.OneToOneField(Question, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def asked_user(self):
        return self.question.asked_user.username

    # @property
    # def formatted_created_at(self):
    #     if self.created_at.year < datetime.datetime.now().year:
    #         return f"{self.created_at.date()}, {self.created_at.year}"
    #     else:
    #         # if (datetime.datetime.now(datetime.timezone.utc) - self.created_at).total_seconds() >= 86400*2:
    #         return f"{self.created_at.strftime('%H:%M, %b %d')}"
    #         # elif (datetime.datetime.now(datetime.timezone.utc) - self.created_at).total_seconds() >= 86400:
    #         #     return f"Yesterday, {str(100+self.created_at.hour)[1:3]}:{str(100+self.created_at.minute)[1:3]}"
    #         # else:
    #         #     return f"Today, {str(100+self.created_at.hour)[1:3]}:{str(100+self.created_at.minute)[1:3]}"

    def __str__(self):
        return ' '.join(self.question.content.split(" ")[:10]) + ' -> ' + ' '.join(self.content.split(" ")[:10])
