from django.urls import path

from app_superstore.views import (
    show_debug,
    show_home,
    show_register,
    show_login
)

urlpatterns = (
    path('', show_home, name='index'),
    path('register/', show_register, name='register'),
    path('login/', show_login, name='login'),
    path('debug/', show_debug, name='debug'),
)
