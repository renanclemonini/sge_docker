from django.contrib import admin
from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # pyrefly: ignore  # bad-override
    list_display = ('title', 'serie_number', 'created_at', 'updated_at',)
    # pyrefly: ignore  # bad-override
    search_fields = ('title',)
