from django.contrib import admin
from django.urls import path, include
from .views import home_view, user_view, QuestionEdit, QuestionDelete, QuestionAnswer, SearchResultsView

urlpatterns = [
    path('', home_view, name="home"),
    path('edit/<int:pk>', QuestionEdit.as_view(), name="question-edit"),
    path('delete/<int:pk>', QuestionDelete.as_view(), name="question-delete"),
    path('answer/<int:pk>', QuestionAnswer.as_view(), name="question-answer"),
    path('search', SearchResultsView.as_view(), name="user-search"),
    path('<str:username>', user_view, name="user"),
    path('users/', include('users.urls'))
]
