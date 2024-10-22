from django.shortcuts import render

# Create your views here.
def ventes(request):
    return render(request, 'ventes/ventes.html') 