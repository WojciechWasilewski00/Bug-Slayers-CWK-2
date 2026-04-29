from django.urls import path, include
from . import views

# Set an app_name to help with namespacing and maintainability 
app_name = 'scheduling'

urlpatterns = [
    # Dashboard - The main view for your individual element
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Creation logic
    path('add/', views.create_meeting, name='create_meeting'),
    
    # Schedule views
    path('schedule/', views.weekly_schedule, name='weekly_schedule'),
    
    # Dynamic Routing for specific meetings (Detail, Edit, Delete)
    # Using <int:pk> ensures the logic targets specific database records
    path('meeting/<int:pk>/', views.meeting_detail, name='meeting_detail'),
    path('meeting/<int:pk>/edit/', views.edit_meeting, name='edit_meeting'),
    path('meeting/<int:pk>/delete/', views.delete_meeting, name='delete_meeting'),
    
    # Integration with group authentication system
    path('accounts/', include('django.contrib.auth.urls')),
]