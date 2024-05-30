from django.urls import path
from .views import *

app_name = 'userauth'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    
]
