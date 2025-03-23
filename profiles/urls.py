from django.urls import path
from . import views
from .views import delete_account

urlpatterns = [
    path('', views.profile, name='profile'),
    path(
        'order_history/<order_number>',
        views.order_history, name='order_history'),
    path("delete_account/", delete_account, name="delete_account"),
]
