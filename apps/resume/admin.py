from django.contrib import admin

from . import models


@admin.register(models.ResumeItem)
class ResumeItemAdmin(admin.ModelAdmin):
    filter_horizontal = ('resumes',)
    list_display = ('user', 'jobTitle', 'company', 'start_date', )
    ordering = ('user', '-start_date')

@admin.register(models.Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', )
    ordering = ('user', 'title')
