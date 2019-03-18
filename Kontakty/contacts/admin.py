from django.contrib import admin
from .models import Person, Adress, Telephone, Email, Groups

# Register your models here.
admin.site.register(Person)
admin.site.register(Adress)
admin.site.register(Telephone)
admin.site.register(Email)
admin.site.register(Groups)
