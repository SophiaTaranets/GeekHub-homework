# users/urls.py
from django.urls import path
from .views import custom_login, custom_logout

app_name = 'users'
urlpatterns = [
    path('login/', custom_login, name='custom_login'),
    path('logout/', custom_logout, name='custom_logout')
]
