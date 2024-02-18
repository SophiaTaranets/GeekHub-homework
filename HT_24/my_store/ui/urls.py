from django.urls import path

from .views import index


app_name = 'ui'

urlpatterns = [
    path('', index, name='index')
]