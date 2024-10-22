from django.shortcuts import render

# Vue pour la gestion des stocks
def gestion_stocks(request):
    return render(request, 'stocks/gestion_stocks.html')
