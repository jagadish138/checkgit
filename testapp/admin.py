from django.contrib import admin
from testapp.models import new_model,new_class
# Register your models here.

class classAdmin(admin.ModelAdmin):
    list_display = ['name','user','age']

admin.site.register(new_model,classAdmin)

class classAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(new_class,classAdmin)