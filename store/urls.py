from django.contrib import admin
from django.urls import path, include
from .views import ProductView

urlpatterns = [
    path('', ProductView.as_view())
]