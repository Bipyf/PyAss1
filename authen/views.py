from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

class TodoLogin(LoginView):
    template_name='authen/login.html'
    fields='__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('task_page')

class RegisterView(FormView):
    template_name = 'authen/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url=reverse_lazy('task_page')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task_page')
        return super(RegisterView, self).get(*args, **kwargs)


class TodoList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user = self.request.user)
        return context
    
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'desc', 'cmpl']
    success_url=reverse_lazy('task_page')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url=reverse_lazy('task_page')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url=reverse_lazy('task_page')