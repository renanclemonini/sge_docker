from django.contrib import admin
from suppliers.models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    # pyrefly: ignore  # bad-override
    list_display = ('name', 'description',)
    # pyrefly: ignore  # bad-override
    search_fields = ('name',)
    # pyrefly: ignore  # bad-override
    ordering = ('name',)
