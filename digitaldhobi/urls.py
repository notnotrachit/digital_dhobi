"""digitaldhobi URL Configuration

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
from orders.views import order, order_detail, order_submit, new_order, completed_order, completed, home, home2


urlpatterns = [
    path('admin/', admin.site.urls),
	path('',home,name="homepage"),
	path('home',home2,name="home"),
    path('accounts/', include('allauth.urls')),	
    path('orders/', order, name='orders'),
	path('completed_order',completed_order),
    path('order_detail/<int:order_id>/', order_detail, name='order_detail'),
    path('new_order/', new_order, name='new_order'),
	path('order_submit',order_submit),
    path('completed/<int:order_id>/', completed, name='completed')
]
