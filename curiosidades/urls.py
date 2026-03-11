from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:curiosidade_id>/', views.detalhe, name='detalhe'),
]