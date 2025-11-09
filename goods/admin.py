from django.contrib import admin
from goods.models import Categories


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug":("name",)}
