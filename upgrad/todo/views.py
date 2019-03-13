from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import todo

def index(request):
	data = todo.objects.all()
	print (data)
	for index, item in enumerate(data):
		print (index, item)
	return render(request, 'index.html', { 'submit': False, 'edit_flag':False })

def submit(request):

    task = request.GET['task']
    time = request.GET['time']
    query = todo(task=task, time=time)
    query.save()

    return render(request, 'index.html', { 'submit': True, 'edit_flag':False })

def view(request):
	data = todo.objects.all()
	to = [str(element) for element in list(data)]
	todo_list = [element.split('*#*') for element in to]
	return render(request, 'view.html', {'list': todo_list, 'rng': range(len(todo_list)), 'del_flag':False })

def edit(request):
	task_e = request.GET['taske']
	time_e = request.GET['timee']
	query = todo.objects.get(task=task_e, time=time_e)
	todo.objects.filter(task=task_e, time=time_e).delete()
	query_data = str(query).split('*#*')

	return render(request, 'index.html', { 'task':query_data[0], 'time':query_data[1], 'edit_flag': True })

def delete(request):
	task_d = request.GET['taskd']
	time_d = request.GET['timed']
	todo.objects.filter(task=task_d, time=time_d).delete()
	data = todo.objects.all()
	to = [str(element) for element in list(data)]
	todo_list = [element.split('*#*') for element in to]
	return render(request, 'view.html', {'list': todo_list, 'rng': range(len(todo_list)), 'del_flag':True })