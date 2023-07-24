from django.db import models

# Create your models here.
NULLABLE = {"null": True, "blank": True}


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    preview = models.ImageField(upload_to='products/', verbose_name='Превью', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Категория")
    cost = models.IntegerField(verbose_name="Цена")
    add_date = models.DateTimeField(**NULLABLE, verbose_name="Дата добавления")
    change_date = models.DateTimeField(**NULLABLE, verbose_name="Дата последнего изменения")

    def __str__(self):
        return f'{self.name} {self.description}, {self.category}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
