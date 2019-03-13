from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import todo

def index(request):
	return render(request, 'index.html', { 'submit': False })

def submit(request):

    task = request.GET['task']
    time = request.GET['time']
    query = todo(task=task, time=time)
    query.save()

    return render(request, 'index.html', { 'submit': True })

def view(request):
	data = todo.objects.all()
	to = [str(element) for element in list(data)]
	todo_list = [element.split('*#*') for element in to]
	return render(request, 'view.html', {'list': todo_list, 'rng': range(len(todo_list)), 'q':data })

def edit(request, id):
	query = todo.objects.get(id=id)
	print (query)
	return HttpResponse(str(list(query)))