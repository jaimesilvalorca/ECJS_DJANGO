"""
URL configuration for tarea1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from aplicacion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('products/', views.products, name="products"),
    path('form/', views.form,name="form"),
    path('register/',views.userForm,name='register'),
    path('addproduct/',views.productForm,name='addproduct'),
    path('signin/',views.signin, name='signin'),
    path('productdetail/<int:product_id>/',views.productDetail,name='productdetail'),
    path('addtocart/<int:product_id>/', views.addToCart, name='addtocart'),
    path('view_cart/', views.viewCart, name='viewcart'),
    path('logout/', views.signout, name='logout'),
    path('checkout/', views.checkout, name='checkout')
    
    
]
