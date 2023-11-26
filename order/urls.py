from . import views
from django.urls import path

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    path("addtocart/<int:id>", views.addtocart, name="addtocart"),
    path("shopcart/", views.shopcart, name="shopocart"),
    path('deletefromcart/<int:id>', views.deletefromcart, name='deletefromcart'),
    path('orderproduct/', views.orderproduct, name='orderproduct'),

]