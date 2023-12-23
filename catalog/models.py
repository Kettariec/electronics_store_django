from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Наименование')
    product_description = models.TextField(verbose_name='Описание продукта')
    product_image =  models.ImageField(upload_to='products/', verbose_name='Изображение',
                                       null=True, blank=True) # может быть null или незаполненным
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    product_price = models.IntegerField(verbose_name='Цена')
    product_date_of_creation = models.DateField(verbose_name='Дата создания')
    product_date_of_change = models.DateField(verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.product_name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('product_name',)


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Категория')
    category_description = models.TextField(verbose_name='Описание категории')
    # created_at = models.CharField(max_length=100, verbose_name='создан',
    #                               null=True, blank=True)

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('category_name',)
