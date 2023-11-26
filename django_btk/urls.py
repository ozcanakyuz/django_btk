"""django_btk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django_btk import settings


urlpatterns = [
    path('', include('home.urls')),
    
#     Uygulama linkleri
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
    path('product/', include('product.urls')),
    path('user/', include('user.urls')),
    path('order/', include('order.urls')),
    path('shop/', include('home.urls')),
    path('detail/', include('home.urls')),
#     Blog linkleri

    path('hakkimizda/', include('home.urls'), name="hakkimizda"),
    path('referanslar/', include('home.urls'), name="referanslar"),
    path('iletisim/', include('home.urls'), name="iletisim"),
    # path("referanslar/", home.views.referanslar name="referanslar"),
    # path("iletisim/", home.views.iletisim name="iletisim"),

#     Ckeditor için
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

# resimlerin veya static dosyaların admin tarafında gösterilmesi için
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)