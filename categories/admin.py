from django.contrib import admin
from categories.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # pyrefly: ignore  # bad-override
    list_display = ('name', 'description', 'created_at', 'updated_at')
    # pyrefly: ignore  # bad-override
    search_fields = ('name',)
    # pyrefly: ignore  # bad-override
    ordering = ('name',)
