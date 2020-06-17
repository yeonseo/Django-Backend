from django.contrib import admin
from . import models

@admin.register(models.BoardType)
class CustomItemTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Comment)
class CustomCommentAdmin(admin.ModelAdmin):
    pass

@admin.register(models.FreeBoard)
class CustomFreeBoardAdmin(admin.ModelAdmin):
    """ Custom FreeBoard Admin """

    list_display = ("username", "title", "created", "views")
    ordering = ("created", "views",)
    list_filter = ("board_type",)

    search_fields = ("=username", "=title")