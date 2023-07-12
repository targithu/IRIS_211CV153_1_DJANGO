from django.shortcuts import render,redirect
from .forms import RegistrationForm,TaskForm,SubTaskForm
from .models import Task,SubTasks
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
def base(request):
 return render(request,'first/base.html')
@login_required(login_url='/login')
def view_tasks(request):
    tasks=Task.objects.all()
    if request.method=="POST":
     task_id=request.POST.get("task-id")
     task=Task.objects.filter(id=task_id).first()
     if task and task.author==request.user:
        task.delete()
    return render(request,'first/view_tasks.html',{"tasks":tasks})
 
@login_required(login_url='/login')
def add_task(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.author=request.user
            task.save()
            return redirect('/view_tasks')
    else:
        form=TaskForm()
    return render(request,'first/add_task.html',{"form":form}) 
@login_required(login_url='/login')
def subtask(request):
    tasks=SubTasks.objects.all()
    if request.method=="POST":
     task_id=request.POST.get("task-id")
     task=SubTasks.objects.filter(id=task_id).first()
     if task and task.author==request.user:
        task.delete()
    return render(request,'first/subtask.html',{"tasks":tasks})
 
@login_required(login_url='/login')
def add_subtask(request):
    if request.method=='POST':
        form=SubTaskForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.author=request.user
            task.save()
            return redirect('/subtask')
    else:
        form=SubTaskForm()
    return render(request,'first/add_subtask.html',{"form":form}) 
def sign_up(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/login')
    else:
        form=RegistrationForm()
    return render(request,'registration/sign_up.html',{"form":form})
    
