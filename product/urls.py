from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("kategori_urunler/", views.index, name="kategori_urunler"),
    path('addcomment/<int:id>', views.addcomment, name="addcomment")
]