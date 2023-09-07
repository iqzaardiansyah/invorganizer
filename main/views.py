from django.shortcuts import render
from .models import Item

def show_main(request):
    context = {
        'name': 'Iqza Ardiansyah',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)

def show_products(request):
    data = {}
    return render(request, "main.html", )