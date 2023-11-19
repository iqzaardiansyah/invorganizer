import json
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse, JsonResponse
from .forms import ItemForm
from django.urls import reverse
from .models import Item
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login')
def show_main(request):
    list = Item.objects.all().filter(user=request.user).order_by('name')
    count = 0
    for item in list:
        count += item.amount
    context = {
        'name': 'Iqza Ardiansyah',
        'class': 'PBP F',
        'list' : list,
        'count': count,
        'last_login': request.COOKIES['last_login'],
        'user':request.user.username,
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("main:show_main"))
    else:
        return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def remove(request, id):
    product = Item.objects.get(pk = id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
    
def decrement(request, id = None):
    object = Item.objects.get(pk = id)
    if object.amount > 1:
        object.amount -= 1
    object.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def increment(request, id = None):
    object = Item.objects.get(pk = id)
    object.amount += 1
    object.save()
    return HttpResponseRedirect(reverse('main:show_main'))


def BacktoMain(request):
    return HttpResponseRedirect(reverse('main:show_main'))

def edit_product(request, id):
    object = Item.objects.get(pk = id)
    form = ItemForm(request.POST or None, instance=object)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def get_product_json(request):
    product_item = Item.objects.filter(user=request.user).order_by("name")
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_product = Item(name=name, price=price, description=description, amount=amount, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_product_ajax(request):
    if request.method == 'POST':
        id = request.POST.get("delete")
        item = Item.objects.get(pk = id)

        item.delete()
        return HttpResponse(b"DELETED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            amount = int(data["amount"]),
            price = int(data["price"]),
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt  
def show_json_user(request):
    data = Item.objects.all().filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")