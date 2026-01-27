from django.shortcuts import render, redirect
from .models import Task, TaskTest
from django.views.generic import DetailView, UpdateView
from .forms import TaskForm, TestForm, forms_tests


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
    


class task_update_view(UpdateView):
    model = Task
    template_name = "tasks/task_show.html"
    


def task_create_view(request):
    
    error = ''
    
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        tests = forms_tests(request.POST)
        
        if task_form.is_valid() and tests.is_valid():
            task = task_form.save(commit=False)  
            task.created_by = request.user
            task.save()
            
            for test in tests:  
                test = test.save(commit=False)
                test.task_id = task.id
                test.save()
            return redirect('tasks')
        
        error = 'Форма была неверна'
      
    task_form = TaskForm()
    tests_form = forms_tests()
    
    context = {
        'task_form': task_form,
        'formset_tests': tests_form,
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
        



    
    
    
    
