from django.contrib import admin
from .models import Task,SubTasks
# Register your models here.
admin.site.register(SubTasks)
admin.site.register(Task)