# Create your models here.
from django.db import models
from django.contrib import admin
from django.core.mail import send_mail


class Contact(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email


admin.site.register(Contact)
    def send_mail(self):
        send_mail(
            "Thank you for contact me!",
            "This is an automatic message. I will answer soon!. Regards, Mario Cano.",
            "marcae7@gmail.com",
            ["marcae7@gmail.com", self.email]
        )