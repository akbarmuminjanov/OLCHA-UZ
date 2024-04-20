from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.
def index(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {
        "category":category,
        "categories":categories,
        "products":products
    }
    return render(request, "index.html", context)