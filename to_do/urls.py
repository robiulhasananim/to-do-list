from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyTemplateHome.as_view(), name='homepage'),
    path('add_tasks/', views.AddTasksFormView.as_view(), name='add_tasks'),
    path('show_tasks/', views.ShowTasksFormView.as_view(), name='show_tasks'),
    path('completed_tasks/', views.CompletedTasksFormView.as_view(), name='completed_tasks'),
    path('delete_tasks/<int:pk>', views.DeleteTasksFormView.as_view(), name='delete_tasks'),
    path('edit_task/<int:pk>', views.TaskUpdateFormView.as_view(), name='edit_task'),
    path('complete_task/<int:pk>', views.completeTask, name='complete_task'),
]
