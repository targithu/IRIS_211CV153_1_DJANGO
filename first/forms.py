from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import SubTasks, Task,Clubs
class RegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
class DateInput(forms.DateInput):
    input_type='date'
class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=["title","description","deadline","socialmedia"]
        widgets={
            'deadline':DateInput(),
        }
class ClubForm(forms.ModelForm):
    class Meta:
        model=Clubs
        fields=["clubselected"]
class SubTaskForm(forms.ModelForm):
    class Meta:
        model=SubTasks
        fields=["title","description","deadlin","status"]
        widgets={
            'deadlin':DateInput(),
        }
