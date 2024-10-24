from django.contrib import admin
from .models import Produit

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'quantite', 'prix', )
    search_fields = ('nom',)  # Permet de rechercher par nom de produit

admin.site.register(Produit, ProduitAdmin)
