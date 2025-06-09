from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_account, name='create_account'),
    path('account/<int:account_id>/', views.view_account, name='view_account'),
    path('add_transaction/add/', views.add_transaction, name='add_transaction'),
]
