
from django.shortcuts import render
from TODO_APP.models import task
def home(request):
    tasks = task.objects.filter(is_completed=False).order_by('-updated_at')
    context = {
        'tasks':tasks,
    }
    return render(request, 'home.html',context)