from django.shortcuts import render

# Create your views here.
def caisse(request):
    return render(request, 'caisse/caisse.html')