from django.contrib import admin

#here we gona register our model so that we can see it admin panel
from .models import Customer
# Register your models here.
admin.site.register(Customer)
