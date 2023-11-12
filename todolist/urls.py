from django.urls import path

from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='tasks'),
    path('create', views.TaskCreate.as_view(), name='create'),
    path('update/<int:pk>', views.TaskUpdate.as_view(), name='update'),
    path('detail/<int:pk>', views.TaskDetail.as_view(), name='detail'),
    path('delete/<int:pk>', views.TaskDelete.as_view(), name='delete')
]