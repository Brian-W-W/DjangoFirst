from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('', views.master, name="master"),
    path('', views.navigation, name="nav" ),
    path('group_one/', views.index, name='index'),
    path('group_one/details/<int:id>', views.details, name='details'),
    ]
