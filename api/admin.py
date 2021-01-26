from django.contrib import admin
from .models import *

admin.site.register(Client)
admin.site.register(BusinessClient)
admin.site.register(Employee)
admin.site.register(PersonalAppointment)
admin.site.register(BusinessAppointment)
admin.site.register(Company)

# Register your models here.
