from django.shortcuts import render 
from django.shortcuts import redirect
# Create your views here.

def creer_un_produit(request) :
    return render (request, 'produit/creer_produit.html')


def modif_un_produit(request) :
    
    return render (request, 'produit/modif_produit.html')

def sup_un_produit(request) :
    return render (request, 'produit/sup_produit.html')

def liste_produit(request) :
    return render (request, 'produit/liste_produit.html')