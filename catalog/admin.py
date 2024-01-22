from django.contrib import admin
from catalog.models import Product, Category


# Register your models here.
# admin.site.register(Product)
# admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админка отображения модели Product"""
    list_display = ('id', 'product_name', 'product_price', 'product_category', 'author',)
    list_filter = ('product_category',)
    search_fields = ('product_name', 'product_description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Админка отображения модели Category"""
    list_display = ('id', 'category_name',)
