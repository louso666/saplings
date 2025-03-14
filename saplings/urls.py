"""
URL configuration for saplings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('', views.index, name='index'),
    path('cart/', include('cart.urls')),  # Корзина
    path('products/', include('products.urls')), # Товары
    path('articles/', include('articles.urls')),  # Подключение маршрутов из articles
    path('profile/', include('accounts.urls')),  # Подключение URLs для профиля
]
