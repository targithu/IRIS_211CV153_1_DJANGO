from django.urls import path
from . import views

urlpatterns = [
    path('',views.none,name='none'),
    path('base/',views.base,name='base'),
    path('home/',views.home,name='home'),
     path('task/',views.task,name='task'),
    path('sign-up/',views.sign_up,name='sign_up'),
]