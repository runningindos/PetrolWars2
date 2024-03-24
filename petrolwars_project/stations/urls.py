from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='stations-home'),
    path('share/',views.share, name='stations-share'),
]