from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('item',views.index),
    path('additem',views.add_item),
    path('product',views.product),
    path('summary',views.summary),
    path('cart/<int:id>',views.add_to_cart),

]
