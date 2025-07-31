from django.contrib import admin
from inflows.models import Inflow


@admin.register(Inflow)
class InflowAdmin(admin.ModelAdmin):
    # pyrefly: ignore  # bad-override
    list_display = ('supplier', 'product', 'quantity', 'created_at', 'updated_at')
    # pyrefly: ignore  # bad-override
    search_fields = ('supplier__name', 'product__title')
    # pyrefly: ignore  # bad-override
    list_filter = ('created_at',)
    # pyrefly: ignore  # bad-override
    ordering = ('-created_at',)
    # pyrefly: ignore  # bad-override
    date_hierarchy = 'created_at'
