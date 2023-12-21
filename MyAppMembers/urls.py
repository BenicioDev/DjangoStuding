from django.urls import path, include
from . import views

urlpatterns = [
    path('membros/', views.membros, name='Membros' )
]