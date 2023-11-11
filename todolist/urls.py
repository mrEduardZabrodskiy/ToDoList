from django.urls import path

from . import views

urlpatterns = [
    path('', views.TaskList.as_view()),
    path('create/', views.CreateTask.as_view(), name='create'),
    path('modify/<int:pk>', views.ModifyTask.as_view(), name='modify'),
    path('delete/<int:pk>', views.DeleteTask.as_view(), name='delete'),
]