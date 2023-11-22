from django.urls import path
from .views import *

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('json/', show_json_user, name='show_json_user'),
]