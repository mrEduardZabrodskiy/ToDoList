from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView,CreateView
from rest_framework.permissions import IsAuthenticated
from django.urls import reverse_lazy

from .models import Task

# Create your views here.

class TaskList(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tasks'


class TaskCreate(CreateView):
    model = Task
    success_url = reverse_lazy('tasks')
    fields = '__all__'
    template_name = 'new_task.html'

    
class TaskDetail(DetailView):
    model = Task
    template_name = 'detail.html'
    
    
class TaskUpdate(UpdateView):
    model = Task
    context_object_name = 'task'
    template_name = 'update.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class TaskDelete(DeleteView):
    model = Task
    success_url = 'tasks'
    context_object_name = 'task'
    template_name = 'delete.html'
    success_url = reverse_lazy('tasks')