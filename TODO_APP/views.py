from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import task
def addTask(request):
    task1 = request.POST['task']
    task.objects.create(task=task1)
    return redirect('home')

def mark_as_done(request, pk):
    task1 = get_object_or_404(task, pk=pk)
    task1.is_completed = True
    task1.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task1 = get_object_or_404(task, pk=pk)
    task1.is_completed = False
    task1.save()
    return redirect('home')

def edit_task(request, pk):
    get_task =get_object_or_404(task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': get_task,
        }
        return render(request, 'edit_task.html',context)

def delete_task(request, pk):
    task1 = get_object_or_404(task, pk=pk)
    task1.delete()
    return redirect('home')