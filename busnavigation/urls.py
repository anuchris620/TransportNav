from django.urls import path
from . import views
#from .views import index, RouteLoadView


urlpatterns = [
    path('', views.index, name='index'),
    path('Route_load/', views.Route_Load, name='Route_Load'),
    path('Map_Load/', views.Map_Load, name='Map_Load'),
    path('trial/', views.home, name='trial'),
    #path('route_load/', RouteLoadView.as_view(), name='Route_Load'),


]

