from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import todo

def index(request):
	data = todo.objects.all()
	print (data)
	for index, item in enumerate(data):
		print (index, item)
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
	return render(request, 'view.html', {'list': todo_list, 'rng': range(len(todo_list)), 'del_flag':False })

def edit(request):
	task = request.GET['taske']
	time = request.GET['timed']
	return HttpResponse(str(task))

def delete(request):
	task_d = request.GET['taskd']
	time_d = request.GET['timed']
	todo.objects.filter(task=task_d, time=time_d).delete()
	data = todo.objects.all()
	to = [str(element) for element in list(data)]
	todo_list = [element.split('*#*') for element in to]
	return render(request, 'view.html', {'list': todo_list, 'rng': range(len(todo_list)), 'del_flag':True })