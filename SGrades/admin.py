from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Item)
admin.site.register(Grade)
admin.site.register(Submit)