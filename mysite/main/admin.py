from django.contrib import admin
from  .models import (IndexCaruselActive,  IndexCarusel, 
                      Category, Brand, Product, Contact,
                      Cart   )
from modeltranslation.admin import TranslationAdmin
# Register your models here.

@admin.register(IndexCaruselActive,  IndexCarusel)
class IndexCaruselActiveAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','name']
    list_display_links = ['id', 'title']
    search_fields = ['id', 'title', 'name']



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']
   
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']    



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email','subject']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']    


admin.site.register(Cart)


