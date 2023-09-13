from django.shortcuts import render
from .models import Item

def show_main(request):
    list = Item.objects.all().order_by("name")
    context = {
        'name': 'Iqzaa Ardiansyah',
        'class': 'PBP F',
        'list' : list
    }

    return render(request, "main.html", context)