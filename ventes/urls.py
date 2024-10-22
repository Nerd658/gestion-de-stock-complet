from django.urls import path
from . import views

urlpatterns = [
    path('', views.ventes, name='ventes'),
]
