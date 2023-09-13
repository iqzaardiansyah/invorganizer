from django.shortcuts import render
from .models import Item

def show_main(request):
    list = Item.objects.all().order_by("name")
    context = {
        'name': 'Iqza Ardiansyah',
        'class': 'PBP F',
        'list' : list
    }

    return render(request, "main.html", context)