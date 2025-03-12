from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('mission/', views.mission, name='mission'),
]
