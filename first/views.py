from django.shortcuts import render, redirect
from .forms import RegistrationForm, TaskForm, SubTaskForm
from .models import Task, SubTasks
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.

def base(request):
    return render(request, 'first/base.html')

@login_required(login_url='/login')
def view_tasks(request):
    tasks = Task.objects.filter(author=request.user)
    if request.method == "POST":
        task_id = request.POST.get("task-id")
        task = Task.objects.filter(id=task_id, author=request.user).first()
        if task:
            task.delete()
    return render(request, 'first/view_tasks.html', {"tasks": tasks})

@login_required(login_url='/login')
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            return redirect('/view_tasks')
    else:
        form = TaskForm()
    return render(request, 'first/add_task.html', {"form": form}) 

@login_required(login_url='/login')
def subtask(request):
    subtasks = SubTasks.objects.filter(task__author=request.user)
    if request.method == "POST":
        subtask_id = request.POST.get("subtask-id")
        subtask = SubTasks.objects.filter(id=subtask_id, task__author=request.user).first()
        if subtask:
            subtask.delete()
    return render(request, 'first/subtask.html', {"subtasks": subtasks})

@login_required(login_url='/login')
def add_subtask(request):
    if request.method == 'POST':
        form = SubTaskForm(request.POST)
        if form.is_valid():
            subtask = form.save(commit=False)
            subtask.save()
            return redirect('/subtask')
    else:
        form = SubTaskForm()

    return render(request, 'first/add_subtask.html', {"form": form})


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('/view_tasks')

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/sign_up.html', {"form": form})

    
