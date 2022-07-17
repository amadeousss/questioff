from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, CreateView, ListView
from .models import Question
from users.models import CustomUser
from .forms import QuestionForm, AnswerForm
from .models import Answer


def home_view(request):
    if request.user.is_authenticated:
        return redirect('user', username=request.user.username)
    else:
        return render(request, 'questions/unauthenticated-home.html')


def user_view(request, username):
    user = CustomUser.objects.get(username=username)
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.asked_user = user
            question.save()
            return HttpResponseRedirect(f"{username}")

    form = QuestionForm()
    latest_questions_unfiltered = Question.objects.filter(asked_user=user)
    latest_questions = []
    if request.user == user:
        latest_questions = latest_questions_unfiltered
    else:
        for q in latest_questions_unfiltered:
            if Answer.objects.filter(question_id=q.id).exists():
                latest_questions.append(q)

    return render(request, 'questions/user.html',
                  {'form': form, 'latest_questions': latest_questions, 'user': user})


class QuestionEdit(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Question
    template_name = 'questions/question-edit.html'

    def test_func(self):
        return self.request.user == self.get_object().asked_user


class QuestionDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Question
    success_url = reverse_lazy("home")

    def test_func(self):
        return self.request.user == self.get_object().asked_user


class QuestionAnswer(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': AnswerForm(), 'question': Question.objects.get(id=self.kwargs['pk'])}
        return render(request, 'questions/question-answer.html', context)

    def post(self, request, *args, **kwargs):
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question_id = self.kwargs['pk']
            answer.save()
            return HttpResponseRedirect(reverse_lazy('home'))
        return render(request, 'questions/question-answer.html',
                      {'form': form, 'question': Question.objects.get(id=self.kwargs['pk'])})

    def test_func(self, *args, **kwargs):
        return self.request.user == Question.objects.get(id=self.kwargs['pk']).asked_user


class SearchResultsView(ListView):
    model = CustomUser
    template_name = 'questions/search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = CustomUser.objects.filter(username__startswith=query)[:5]
        return object_list
