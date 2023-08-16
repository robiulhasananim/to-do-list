from django.shortcuts import render, redirect
from django.db.models.query import QuerySet
from to_do.forms import TaskForm
from to_do.models import TaskModel
from django.views.generic import TemplateView, ListView, UpdateView
from django.views.generic.edit import DeleteView, CreateView
from django.urls import reverse_lazy

# Create your views here.

class MyTemplateHome(TemplateView):
    template_name = 'home.html'

class AddTasksFormView(CreateView):
    model = TaskModel
    template_name = 'add_tasks.html'
    form_class = TaskForm
    success_url = '/show_tasks'
    
class ShowTasksFormView(ListView):
    model = TaskModel
    template_name = 'show_tasks.html'
    context_object_name = 'data'

class CompletedTasksFormView(ListView):
    model = TaskModel
    template_name = 'completed_tasks.html'
    context_object_name = 'data'

class DeleteTasksFormView(DeleteView):
    model = TaskModel
    template_name = 'delete_confirmation.html'
    success_url = reverse_lazy('show_tasks')

class TaskUpdateFormView(UpdateView):
    model = TaskModel
    template_name = 'add_tasks.html'
    form_class = TaskForm
    success_url = reverse_lazy('show_tasks')
    
    
def completeTask(request, pk):
    task = TaskModel.objects.get(id=pk)
    task.is_completed = True
    task.save()
    return redirect("completed_tasks")
    
    

