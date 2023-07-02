from django.shortcuts import render
from django.http import HttpResponse
from email_send.tasks import celery_email
# Create your views here.
def send_mail_all(request):
    celery_email.delay()
    return HttpResponse("Sent")