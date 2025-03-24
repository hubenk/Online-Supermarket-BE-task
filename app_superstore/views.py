from django.shortcuts import render, redirect

import pandas as pd

from app_superstore.forms import UserProfileForm
from app_superstore.models import Product, UserProfile


def show_home(request):
    return render(request, 'main.html')


def show_register(request):
    form = None
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("profile_success")
        else:
            form = UserProfileForm()

    return render(request, 'register.html', {'form': form})


def show_login(request):
    return render(request, 'login.html')


def show_debug(request):
    users = UserProfile.objects.all()
    user_data = pd.DataFrame(users.values())

    products = Product.objects.all()
    product_data = pd.DataFrame(products.values())

    context = {
        'users': user_data.to_html(index=False),
        'products': product_data.to_html(index=False)
    }

    return render(request, 'debug.html', context)
