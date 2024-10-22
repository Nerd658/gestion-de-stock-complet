from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_produit, name='liste_produit'),
    path('creer_un_produit/', views.creer_un_produit, name='creer_un_produit'),
    path('modif_un_produit/', views.modif_un_produit, name='modif_un_produit'),
    path('sup_un_produit/', views.sup_un_produit, name='sup_un_produit'),
]
