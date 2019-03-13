from django.core.mail import send_mail
from django.shortcuts import render

def mail(task, time, email):
	send_mail(
    'Task alert',
    'Kindly perform' + str(task) + 'as it is scheduled at' + str(time),
    'admin@somedomain.com',
    [str(email)],
    fail_silently=False,
	)
