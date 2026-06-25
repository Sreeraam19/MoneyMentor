from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('analytics/', views.analytics_page, name='analytics_page'),
    path('api/analytics/', views.analytics_api, name='analytics_api'),
    path('api/transactions/add/', views.add_transaction, name='add_transaction'),
]
