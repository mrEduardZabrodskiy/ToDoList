from typing import Any
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from rest_framework.permissions import IsAuthenticated
from django.urls import reverse_lazy

from .models import Task

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks')


class CustomLogoutView(LogoutView):
    
    def get_success_url(self):
        return reverse_lazy('tasks')


class RegistrationView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistrationView, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegistrationView, self).get(*args, **kwargs)
    
class TaskList(LoginRequiredMixin ,ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(status=False).count()
        return context


class TaskCreate(LoginRequiredMixin ,CreateView):
    model = Task
    success_url = reverse_lazy('tasks')
    fields = ['title', 'description', 'status']
    template_name = 'new_task.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

    
class TaskDetail(LoginRequiredMixin ,DetailView):
    model = Task
    template_name = 'detail.html'
    
    
class TaskUpdate(LoginRequiredMixin ,UpdateView):
    model = Task
    context_object_name = 'task'
    template_name = 'update.html'
    fields = ['title', 'description', 'status']
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskUpdate, self).form_valid(form)
    
    
class TaskDelete(LoginRequiredMixin ,DeleteView):
    model = Task
    success_url = 'tasks'
    context_object_name = 'task'
    template_name = 'delete.html'
    success_url = reverse_lazy('tasks')