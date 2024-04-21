from django.urls import path

from .views import index, product_detail
# app_name = 'product'

urlpatterns = [
    path("", index, name="index"),
    path(r'^(?P<category_slug>[-\w]+)/$', index, name='product_list_by_category'),
    path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', product_detail, name='product_detail'),
]
