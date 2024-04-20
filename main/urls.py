from django.urls import path

from .views import index

urlpatterns = [
    path("", index, name="index"),
    path(r'^(?P<category_slug>[-\w]+)/$', index, name='product_list_by_category'),
]
