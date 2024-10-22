from django.shortcuts import render

# Create your views here.

# Vue pour le tableau de bord
def dashboard(request):
    return render(request, 'utilisateurs/dashboard.html')
