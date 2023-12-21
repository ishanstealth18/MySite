from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import TodoForm
from .models import Todo
# Create your views here.


def index(request):

    # Display tasks
    todo_data = Todo.objects.all().values()
    context = {
        'todo_data': todo_data
        }

    if request.method == 'POST':
        #todo_form = TodoForm(request.POST)
        #if todo_form.is_valid():
            #todo_form.save()
        todo_data = Todo()
        todo_data.title = request.POST.get('title')
        todo_data.details = request.POST.get('description')
        todo_data.date = request.POST.get('date')
        todo_data.save()

        home_template = loader.get_template('home.html')

    return render(request, 'home.html', context)


def delete_task(request, item_id):
    task_to_delete = Todo.objects.get(id=item_id)
    task_to_delete.delete()
    return redirect('home')

