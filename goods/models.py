from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URL')

    class Meta:
        verbose_name="Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
    
class Products(models.Model):
    name = models.CharField(max_length = 150, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to="images/",verbose_name='Изображение', blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name="Скидка")
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    slug = models.SlugField(blank=True, null=True, max_length=150, unique=True, verbose_name='URL')
    category = models.ForeignKey(Categories, on_delete = models.PROTECT, verbose_name='Категория')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = "Продукты"

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100,2)
        return self.price

    def __str__(self):
        return self.name