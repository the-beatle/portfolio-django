# Create your models here.
from django.db import models
from django.contrib import admin


class Contact(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email


admin.site.register(Contact)