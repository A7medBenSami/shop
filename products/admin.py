from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','category','is_active','adding_date','stock']
    search_fields = ['name','price','category','is_active','adding_date','stock']
    list_editable = ['price','category','is_active','stock']
    list_filter = ['name','price','category','is_active','adding_date','stock']
    date_hierarchy = 'adding_date'
    class Meta:
        model = Product


admin.site.register(Product,ProductAdmin)


