from django.db import models

# Create your models here.
class TaskModel(models.Model):
    id = models.IntegerField(primary_key=True)
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False) 
    