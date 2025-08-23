from django.contrib import admin
from . import models


@admin.register(models.AIResult)
class AIResultAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'result',)
