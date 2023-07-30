from django.urls import path
from . import views

urlpatterns = [
    path('',views.base,name='base'),
    path('view_tasks/',views.view_tasks,name='view_tasks'),
    path('add_task',views.add_task,name='add_task'),
    path('subtask/<int:task_id>/', views.subtask, name='subtask'),
    path('add_subtask/<int:task_id>/', views.add_subtask, name='add_subtask'),
    path('sign_up',views.sign_up,name='sign_up'),
]
