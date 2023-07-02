from django.urls import path
from . import views

urlpatterns = [
    path('base/',views.base,name='base'),
    path('view_tasks/',views.view_tasks,name='view_tasks'),
    path('add_task/',views.add_task,name='add_task'),
     path('subtask/',views.subtask,name='subtask'),
    path('add_subtask/',views.add_subtask,name='add_subtask'),
    path('',views.sign_up,name='sign_up'),
]
