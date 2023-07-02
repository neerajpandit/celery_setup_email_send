# from .models import Widget
from django.contrib.auth import get_user_model
from celery import shared_task
from celery_email import settings
from django.core.mail import send_mail
@shared_task(bind=True)
def celery_email(self):
    users=get_user_model.objects.all()
    for user in users:
        mail_subject= "Hi! celery Testing"
        message = "Now I am learn Testing celery"
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email,],
            fail_silently=True,
        )
    return "Done"