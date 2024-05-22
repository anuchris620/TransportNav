from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('Route_load/', views.Route_Load, name='Route_Load'),
    path('Map_Load/', views.Map_Load, name='Map_Load'),


]

