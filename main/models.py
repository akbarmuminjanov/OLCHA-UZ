from django.db import models
from django.urls import reverse
from .utils import create_new_id
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("product_list_by_category", args=[self.slug])
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ("-name",)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    product_kod = models.CharField(max_length=11, editable=False, unique=True, default=create_new_id)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    credit = models.DecimalField(max_digits=14, decimal_places=2)
    quantity = models.PositiveBigIntegerField(default=0)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.id, self.slug])
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="mahsulot")

class Specifications(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specifications = models.CharField(max_length=255)