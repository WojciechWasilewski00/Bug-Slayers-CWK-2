from django.urls import path
from . import views

urlpatterns = [
    path('organisation/', views.organisation_overview, name='organisation_overview'),
    path('department/<int:pk>/', views.department_detail, name='department_detail'),
    path('team/<int:pk>/', views.team_detail, name='team_detail'),
]