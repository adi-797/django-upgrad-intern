from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import todo

def sort(todo_list):
	todo_list = sorted(todo_list, key=lambda l:l[1])
	return todo_list
	

def index(request):
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
	todo_list = sort(todo_list)

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
	todo_list = sort(todo_list)

	return render(request, 'view.html', {'list': todo_list, 'rng': range(len(todo_list)), 'del_flag':True })

def done(request):
	task_do = request.GET['taskdo']
	time_do = request.GET['timedo']
	query = todo.objects.get(task=task_do, time=time_do)
	query_data = str(query).split('*#*')
	todo.objects.filter(task=task_do, time=time_do).delete()
	query = todo(task=query_data[0], time=query_data[1], done='y')
	query.save()
	data = todo.objects.all()
	to = [str(element) for element in list(data)]
	todo_list = [element.split('*#*') for element in to]
	todo_list = sort(todo_list)

	return render(request, 'view.html', {'list': todo_list, 'rng': range(len(todo_list)), 'del_flag':False })

def notdone(request):
	task_ndo = request.GET['taskndo']
	time_ndo = request.GET['timendo']
	query = todo.objects.get(task=task_ndo, time=time_ndo)
	query_data = str(query).split('*#*')
	todo.objects.filter(task=task_ndo, time=time_ndo).delete()
	query = todo(task=query_data[0], time=query_data[1], done='n')
	query.save()
	data = todo.objects.all()
	to = [str(element) for element in list(data)]
	todo_list = [element.split('*#*') for element in to]
	todo_list = sort(todo_list)

	return render(request, 'view.html', {'list': todo_list, 'rng': range(len(todo_list)), 'del_flag':False })