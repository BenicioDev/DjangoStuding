from django.urls import path
from . import views

urlpatterns = [
    path('membros/', views.membros, name='membros' ),
    path('membros/detalhes/<int:id>', views.detalhes, name='detalhes'),
]