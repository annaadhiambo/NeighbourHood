from django.contrib import admin
from .models import Neighbourhood, healthservices, notifications, Business, Health, Authorities, Profile


# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(Health)
admin.site.register(Business)
admin.site.register(healthservices)
admin.site.register(Authorities)
admin.site.register(Profile)
admin.site.register(notifications)
