from django.contrib import admin
from blog.models import Blog


# Register your models here.
# admin.site.register(Product)
# admin.site.register(Category)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """Админка отображения модели Blog"""
    list_display = ('id', 'title', 'body', 'image', 'date_of_creation',)
    list_filter = ('title',)
    search_fields = ('title', 'body',)
