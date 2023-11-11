from django.shortcuts import render
from rest_framework import generics

from .models import Task
from .serializers import TaskSerializer

# Create your views here.


class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    template_name = 'index.html'
    
    def get(self, request):
        data = Task.objects.all()
        print(self.queryset)
        return render(request, self.template_name, {'data': data})

    
class CreateTask(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    
class ModifyTask(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class DeleteTask(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer