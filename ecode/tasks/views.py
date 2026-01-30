from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, TaskTest
from django.views.generic import DetailView, UpdateView
from .forms import TaskForm, TestForm, forms_tests
from django.db import transaction

def tasks_view(request):
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html", {"tasks": tasks})


def task_show(request, pk):
    task = Task.objects.get(id=pk)
    tests = TaskTest.objects.filter(task_id=pk)
    context = {
        "task": task,
        "tests": tests
    }
    return render(request, "tasks/task_show.html", context)
    


def task_update(request, pk):
    error = ""
    task = get_object_or_404(Task, id=pk)
    
    if request.method == "POST":
        task_form = TaskForm(request.POST, instance=task)
        tests_form = forms_tests(request.POST, instance=task)
        if task_form.is_valid() and tests_form.is_valid():
            with transaction.atomic():
                task_form.save()
                tests_form.save()
            return redirect("task-show", pk=pk)
        error = 'Форма была неверна'   
    else:
        task_form = TaskForm(instance=task)
        tests_form = forms_tests(instance=task)
           
    context = {
        "task_form": task_form,
        "tests_form": tests_form,
        'error': error
    }
    
    return render(request,"tasks/task_update.html", context)
    


def task_create_view(request):
    error = ''
    
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        tests_form = forms_tests(request.POST)     
        if task_form.is_valid() and tests_form.is_valid():
            with transaction.atomic():   
                task = task_form.save(commit=False)  
                task.created_by = request.user
                task.save()
                
                tests_form.instance = task
                tests_form.save()
            return redirect('tasks')
        
        error = 'Форма была неверна'
    else:
        task_form = TaskForm()
        tests_form = forms_tests()
    
    context = {
        'task_form': task_form,
        'tests_form': tests_form,
        'error': error
    }
    
    return render(request, 'tasks/task_create.html', context)

def task_delete_view(request, pk):
    error = ''
    
    try:
        task = Task.objects.get(id=pk)
        task.delete()
        return redirect('tasks')
    
    except Task.DoesNotExist:
        error = "Задача не найдена"
        return redirect('tasks', {'error': error})
        



    
    
    
    
