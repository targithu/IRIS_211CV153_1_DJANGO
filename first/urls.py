from django.urls import path
from . import views

urlpatterns = [
    path('',views.none,name='none'),
    path('case/',views.base,name='base'),
    path('base/',views.base,name='base'),
    path('home/',views.home,name='home'),
    path('task/',views.task,name='task'),
     path('subtask/',views.subtask,name='subtask'),
    path('subtasks/',views.subtasks,name='subtasks'),
    path('sign-up/',views.sign_up,name='sign_up'),
]