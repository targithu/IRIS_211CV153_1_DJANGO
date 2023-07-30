from django.shortcuts import render, redirect,get_object_or_404
from .forms import RegistrationForm, TaskForm, SubTaskForm
from .models import Task, SubTasks
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.
def base(request):
    features = [
        {
            'title': 'User Authentication',
            'description': 'User registration and login with authentication.',
        },
        {
            'title': 'Dashboard Display',
            'description': 'Dashboard displaying club-specific tasks and subtasks.',
        },
        {
            'title': 'Create,View,Delete tasks',
            'description': 'Create, view, and delete tasks with associated details such as title, description, deadline, and social media platform.',
        },
        {
            'title': 'Add Subtasks',
            'description': 'Add subtasks to tasks, providing additional details and descriptions thus allowing for more efficient task management.',
        },
    ]

    return render(request, 'first/base.html', {'features': features})


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
def subtask(request, task_id):
    task = Task.objects.get(id=task_id)
    subtasks = SubTasks.objects.filter(task=task)
    return render(request, 'first/subtask.html', {"subtasks": subtasks,"task": task })

@login_required(login_url='/login')
def add_subtask(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = SubTaskForm(request.POST)
        if form.is_valid():
            subtask = form.save(commit=False)
            subtask.task = task 
            subtask.save()
            return redirect('subtask', task_id=task_id)
    else:
        form = SubTaskForm()

    return render(request, 'first/add_subtask.html', {"form": form, "task": task})

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

    
