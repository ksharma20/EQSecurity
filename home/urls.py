from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('stock/<pk>', views.stock, name='stock'),
]
