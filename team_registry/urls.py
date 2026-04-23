from django.urls import path
from . import views

urlpatterns = [
    # Organisation
    path('organisation/', views.organisation_overview, name='organisation_overview'),

    # Departments
    path('department/<int:pk>/', views.department_detail, name='department_detail'),
    path('department/create/', views.department_create, name='department_create'),
    path('department/<int:pk>/edit/', views.department_edit, name='department_edit'),
    path('department/<int:pk>/delete/', views.department_delete, name='department_delete'),

    # Teams
    path('team/<int:pk>/', views.team_detail, name='team_detail'),
    path('team/create/', views.team_create, name='team_create'),
    path('team/<int:pk>/edit/', views.team_edit, name='team_edit'),
    path('team/<int:pk>/delete/', views.team_delete, name='team_delete'),

    # Team Types
    path('teamtype/', views.teamtype_list, name='teamtype_list'),
    path('teamtype/create/', views.teamtype_create, name='teamtype_create'),
    path('teamtype/<int:pk>/edit/', views.teamtype_edit, name='teamtype_edit'),
    path('teamtype/<int:pk>/delete/', views.teamtype_delete, name='teamtype_delete'),

    # Dependencies
    path('dependencies/', views.dependency_list, name='dependency_list'),
    path('dependency/create/', views.dependency_create, name='dependency_create'),
    path('dependency/<int:pk>/edit/', views.dependency_edit, name='dependency_edit'),
    path('dependency/<int:pk>/delete/', views.dependency_delete, name='dependency_delete'),
]