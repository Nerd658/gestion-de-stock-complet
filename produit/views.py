from django.shortcuts import render 
from django.shortcuts import redirect
from .models import Produit
from django.shortcuts import get_object_or_404
# Create your views here.

def creer_un_produit(request) :
    if request.method == "POST" :
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        prix = request.POST.get('prix')
        quantite = request.POST.get('quantite')
        
        if nom and prix and quantite :
            Produit.objects.create(
                quantite=quantite,
                nom=nom,
                prix=prix,
                
            )
        return redirect ('liste_produit')
    
    return render (request, 'produit/creer_produit.html')


def modif_produit(request, produit_id) :
    
    if request.method == 'POST' :
        produit = get_object_or_404(Produit , id=produit_id)
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        prix = request.POST.get('prix')
        quantite = request.POST.get('quantite')
        
        produit.nom = nom,
        produit.description = description,
        produit.prix = prix,
        produit.quantite = quantite,
        
        produit.save()
        
        return redirect ('liste_produit')
        
    
    return render (request, 'produit/modif_produit.html')

def sup_produit(request, produit_id) :
    
    if request.method == 'POST' :
        produit = get_object_or_404(Produit, id=produit_id)
        produit.delete()
        return redirect('liste_produit')
    
    return render(request, 'produit/sup_produit.html')





def liste_produit(request):
    produits = Produit.objects.all()  # Récupère tous les produits
    total_produits = produits.count()  # Compte total des produits
    valeur_stock = sum([p.quantite * p.prix for p in produits])  # Calcule la valeur du stock
    
    for produit in produits :
        produit.prix_total = produit.quantite*produit.prix
        
    return render(request, 'produit/liste_produit.html', {
        'produits': produits,
        'total_produits': total_produits,
        'valeur_stock': valeur_stock
    })