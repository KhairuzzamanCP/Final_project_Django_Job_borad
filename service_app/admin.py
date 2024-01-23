from django.contrib import admin
from service_app.models import ServiceModel


# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('service',)}
    list_display = ['service', 'slug']
admin.site.register(ServiceModel,ServiceAdmin)