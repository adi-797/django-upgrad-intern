import datetime, celery
from .models import todo
from rest import *

intial_time = int(str(datetime.datetime.now())[-15:-13]) #to get hours only
usermail = 'dummy@domainname.com'

@celery.decorators.periodic_task(run_every=datetime.timedelta(minutes=10)) #run every 10 minutes.

def myTask():
    data = todo.objects.all()
    to = [str(element) for element in list(data)]
	todo_list = [element.split('*#*') for element in to]

	for index in range(len(todo_list)):
		if todo_list[index][1][:2] == hour and ((todo_list[index][1][3:5] - 10 < min) and (todo_list[index][1][3:5] + 10) > min):
			mail(todo_list[index][0], todo_list[index][1], usermail)

	# if abs(int(str(datetime.datetime.now())[-15:-13]) - intial_time) > 10:
	# 	for index in range()


