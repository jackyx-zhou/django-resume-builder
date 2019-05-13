from django.contrib import admin

from . import models


@admin.register(models.ResumeItem)
class ResumeItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'jobTitle', 'company', 'start_date')
    ordering = ('user', '-start_date')

class BookInline(admin.TabularInline):
    model = models.ResumeItem

@admin.register(models.Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('user', 'title')
    inlines = [
        BookInline,
    ]
    ordering = ('user', 'title')
