from django.urls import path
from .views import *

app_name = 'lms'


urlpatterns = [
    path('courses', courseview, name='course')
]
