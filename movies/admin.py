from django.contrib import admin
from . import models

# @admin.register(models.Movie)
class CustomMovieAdmin(admin.ModelAdmin):
    """ Custom Movie Admin """

    list_display = ("id", "title", "genre", "year")
    list_filter = ()