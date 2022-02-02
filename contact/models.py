# Create your models here.
from django.db import models


class Contact(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email
