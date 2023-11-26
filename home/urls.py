from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hakkimizda/", views.hakkimizda, name="hakkimizda"),
    path("referanslar/", views.referanslar, name="referanslar"),
    path("iletisim/", views.iletisim, name="iletisim"),
    path("category/<int:id>/<slug:slug>", views.categoryProducts, name="categoryProducts"),
    path("product_detail/<int:id>/<slug:slug>", views.productDetail, name="productDetail"),
    path('search/', views.search, name='search'),
    path('logout',views.logout_view, name= 'logout_view'),
    path('login', views.login_view, name='login_view'),
    path('signup', views.signup_view, name='signup_view'),

    path("shop/", views.shop, name="shop"),
    path("detail/", views.detail, name="detail"),

]