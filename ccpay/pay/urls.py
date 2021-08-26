from . import views
from django.urls import path

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('payment_cancel/', views.payment_cancel, name='payment_cancel'),
]