from django.contrib import admin
from app import models

admin.site.register(models.Album)
admin.site.register(models.Song)
