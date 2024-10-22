from django.db import models

# Create your models here.

class Produit(models.Model) :
    nom = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True , blank=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite = models.PositiveIntegerField()
    date_ajout = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nom