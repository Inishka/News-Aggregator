from django.contrib import admin
from NewsApplication.models import service

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_icon','service_tittle','service_des')
    
admin.site.register(service,ServiceAdmin)