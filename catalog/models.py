from django.db import models

# Create your models here.
NULLABLE = {"null": True, "blank": True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    preview = models.ImageField(upload_to='products/', verbose_name='Превью', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, **NULLABLE, verbose_name="Категория")
    cost = models.IntegerField(verbose_name="Цена")
    add_date = models.DateTimeField(**NULLABLE, verbose_name="Дата добавления")
    change_date = models.DateTimeField(**NULLABLE, verbose_name="Дата последнего изменения")

    def __str__(self):
        return f'{self.name} {self.description}, {self.category}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Blogpost(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='Адрес', **NULLABLE)
    content = models.TextField(verbose_name='Пост')
    preview = models.ImageField(upload_to='blog/', verbose_name='Превью', **NULLABLE)
    add_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления", **NULLABLE)
    is_published = models.BooleanField(default=True, verbose_name="В список опубликованных")
    showed = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.title} {self.content}'

    class Meta:
        verbose_name = 'Блоговая запись'
        verbose_name_plural = 'Блоговые записи'


class Version(models.Model):
    number = models.IntegerField(verbose_name='номер')
    name = models.CharField(max_length=150, verbose_name='название версии')
    sign = models.TextField(verbose_name='признак версии', **NULLABLE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, **NULLABLE, verbose_name='продукт')

    def __str__(self):
        return f'{self.number} {self.name}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
