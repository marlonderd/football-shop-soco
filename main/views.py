from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Sum
from django.http import HttpResponseRedirect, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
import json

def show_main(request):
    product_filter = request.GET.get('filter')
    if product_filter == 'my':
        products = Product.objects.filter(user=request.user)
    else:
        products = Product.objects.all()

    category_filter = request.GET.get('category')
    if category_filter in ['shoes', 'clothes', 'accessories']:
        products = products.filter(category=category_filter)

    user_products_count = 0
    user_products_total_views = 0
    if request.user.is_authenticated:
        user_products = Product.objects.filter(user=request.user)
        user_products_count = user_products.count()
        aggregation = user_products.aggregate(total_views=Sum('product_views'))
        user_products_total_views = aggregation['total_views'] or 0

    context = {
        'name': 'Marlond Leanderd Batara',
        'npm': '2406486201',        
        'class': 'PBP E',            
        'product_list': products,
        'last_login': request.COOKIES.get('last_login', '-'),
        'active_category': category_filter,
        'user_products_count': user_products_count,
        'user_products_total_views': user_products_total_views,
    }
    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
    
    context = {'form':form}
    return render(request, "create_product.html", context)

def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product':product
    }

    return render(request, "product_detail.html", context)

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)

    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form,
        'product': product
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    category_filter = request.GET.get('category')

    product_list = Product.objects.all()

    if category_filter in ['shoes', 'clothes', 'accessories']:
        product_list = product_list.filter(category=category_filter)

    data = [
        {
            'pk': product.pk,
            'name': product.name,
            'price': str(product.price),
            'stock': product.stock,
            'description': product.description,
            'category': product.get_category_display(),
            'thumbnail': product.thumbnail,
            'created_at': product.created_at.strftime("%d %B %Y"),
            'user': product.user.username if product.user else None,
            'is_hot': product.is_product_hot,
            'product_views': product.product_views,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
        product = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'pk': product.pk,
            'name': product.name,
            'price': str(product.price),
            'stock': product.stock,
            'description': product.description,
            'category': product.get_category_display(),
            'thumbnail': product.thumbnail,
            'created_at': product.created_at.strftime("%d %B %Y"),
            'user': product.user.username if product.user else None,
            'is_hot': product.is_product_hot,
            'product_views': product.product_views,
        }
        return JsonResponse(data)

    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

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
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
@login_required(login_url='/login')
def add_product_ajax(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.user = request.user
            new_product.save()

            return JsonResponse({
                "status": "success",
                "message": "Product added successfully!",
                "product_pk": new_product.pk, 
            }, status=201)
        else:
            return JsonResponse({
                "status": "error",
                "errors": form.errors,
            }, status=400)
    
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)

@csrf_exempt
def register_ajax(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True, "message": "Registration successful!"}, status=201)
        else:
            errors = form.errors.get_json_data()
            return JsonResponse({"success": False, "message": str(errors)}, status=400)
    return JsonResponse({"success": False, "message": "Invalid request method"}, status=405)


@csrf_exempt
def login_ajax(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return JsonResponse({
                "success": True,
                "message": "Login successful!",
                "username": user.username
            }, status=200)
        else:
            errors = form.errors.get_json_data()
            return JsonResponse({"success": False, "message": str(errors)}, status=400)
    return JsonResponse({"success": False, "message": "Invalid request method"}, status=405)

@csrf_exempt
@login_required(login_url='/login')
def edit_product_ajax(request, id):
    try:
        product = Product.objects.get(pk=id, user=request.user)
    except Product.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Product not found or you don't have permission to edit it."}, status=404)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "success", "message": "Product updated successfully!"}, status=200)
        else:
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)
    
    elif request.method == 'GET':
        data = {
            'pk': product.pk,
            'name': product.name,
            'price': product.price,
            'stock': product.stock,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
        }
        return JsonResponse(data)

    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)

@csrf_exempt
@login_required(login_url='/login')
def delete_product_ajax(request, id):
    if request.method == 'POST':
        try:
            product = Product.objects.get(pk=id, user=request.user)
            product.delete()
            return JsonResponse({"status": "success", "message": "Product deleted successfully!"}, status=200)
        except Product.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Product not found or you don't have permission to delete it."}, status=404)
    
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)

@csrf_exempt
def logout_ajax(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({"status": "success", "message": "You have been logged out."}, status=200)
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)

# Create your views here.
