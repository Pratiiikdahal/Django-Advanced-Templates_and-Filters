from django.contrib import admin
from firstapp.models import *
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('fname','lname')
    list_per_page=15