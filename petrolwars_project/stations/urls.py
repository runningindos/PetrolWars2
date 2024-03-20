from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='stations-name'),
    path('share/',views.share, name='blog-share'),
]