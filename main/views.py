from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Iqza Ardiansyah',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)