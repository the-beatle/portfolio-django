from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from category.models import Category

admin.site.register(Category, MPTTModelAdmin)