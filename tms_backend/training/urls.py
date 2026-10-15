from django.urls import path
from .views import TaskListView,TaskDetailView,TaskSubmissionsView

urlpatterns = [
    path('tasks/', TaskListView.as_view(),name='get_all_tasks'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name = 'task_detail'),
    path('tasks/<int:pk>/submissions', TaskSubmissionsView.as_view(), name = 'task_submitted')
]