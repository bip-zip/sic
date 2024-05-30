from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('info.urls')),
    path('lms/', include('lms.urls')),
    path('auth/', include('userauth.urls')),
]
