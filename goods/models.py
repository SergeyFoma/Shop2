from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URL')

    class Meta:
        verbose_name="Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
    

