from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Image) #d
class ImageAdmin(admin.ModelAdmin):
    pass #null class

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Comment)
class CommantAdmin(admin.ModelAdmin):
    pass