from django.contrib import admin
from to_do.models import TaskModel
# Register your models here.
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'taskTitle', 'taskDescription', 'is_completed')
admin.site.register(TaskModel, TaskModelAdmin)