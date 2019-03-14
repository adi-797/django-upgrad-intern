from django.core.mail import send_mail
from django.http import HttpResponse

def mail(task, time, email):
	send_mail(
    'Task alert',
    'Kindly perform' + str(task) + 'as it is scheduled at' + str(time),
    'admin@somedomain.com',
    [str(email)],
    fail_silently=False,
	)


def send_alert(done, pending):
	ret = 'DONE: '
	for element in done:
		ret += element + ' | '
	ret += '\n\n\n'

	for element in pending:
		ret += element + ' | '
		
	return HttpResponse(ret)