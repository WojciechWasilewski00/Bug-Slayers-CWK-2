from django.urls import path
from . import views 

urlpatterns = [
    path('teams/', views.team_page, name='team_page'),
    path('teams/<int:pk>/', views.team_detail, name='team_detail'),
]