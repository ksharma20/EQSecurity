from django.urls import path
from . import views

urlpatterns = [
    path('refresh/', views.refresh),
    path('stock/<pk>/', views.stock),
    path('bhav/<pk>/', views.bhav),
]

