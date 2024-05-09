from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Client)
admin.site.register(models.Pet)
admin.site.register(models.PetSize)
admin.site.register(models.Specie)
admin.site.register(models.Breed)
admin.site.register(models.Services_Names)
admin.site.register(models.Services)
admin.site.register(models.Appointment)
