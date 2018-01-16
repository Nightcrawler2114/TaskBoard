from django.urls import path, include
from .views import TaskListView, TaskCreateView, TaskDeleteView, TaskUpdateView

app_name = 'task'

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('add-note/', TaskCreateView.as_view(), name='create_task'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='delete_task'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='update_task'),
]