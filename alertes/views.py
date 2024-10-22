from django.shortcuts import render

# Create your views here.
def alertes(request):
    return render(request, 'alertes/alertes.html')