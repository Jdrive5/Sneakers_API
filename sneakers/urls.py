from django.urls import path
from . import views

urlpatterns = [
    path('', views.sneakers_list),
]