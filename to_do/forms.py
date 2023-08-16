from django import forms
from to_do.models import TaskModel
class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['taskTitle', 'taskDescription']
        labels = {
            'taskTitle' : 'Task Title',
            'taskDescription' : 'Task Description',
        }
        
    