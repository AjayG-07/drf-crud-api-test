from django.contrib import admin
from api.models import CategoryModel,ProductModel
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','name']

admin.site.register(CategoryModel,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','descriptions','category']

admin.site.register(ProductModel,ProductAdmin)