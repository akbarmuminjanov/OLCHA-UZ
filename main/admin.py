from django.contrib import admin
from .models import Category, Product, ProductImage, Specifications
# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = ProductImage

class SpecificationsInline(admin.TabularInline):
    model = Specifications

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "product_kod", "category"]
    search_fields = ["product_kod", 'category']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline, SpecificationsInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}