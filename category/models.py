# Create your models here.
from django.contrib import admin

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    active = models.BooleanField(default=False)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


admin.site.register(Category)