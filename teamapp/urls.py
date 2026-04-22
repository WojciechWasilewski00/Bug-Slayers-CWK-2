from django.urls import path
from . import views # This "." means "look in the current folder"

urlpatterns = [
    path('teams/', views.team_list, name='team_list'),
    path('teams/<int:pk>/', views.team_detail, name='team_detail'), # Move the path here!
]