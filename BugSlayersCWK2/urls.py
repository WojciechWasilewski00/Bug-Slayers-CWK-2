"""
URL configuration for BugSlayersCWK2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views  # Ensure you have dashboard_view and home_redirect in your project's views.py

urlpatterns = [
    # 1. Admin Panel
    path('admin/', admin.site.urls),
    
    # 2. Authentication (Login/Logout)
    # This provides: /accounts/login/ and /accounts/logout/
    path('accounts/', include('django.contrib.auth.urls')), 
   

    # 3. Core Navigation
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('', views.home_redirect, name='home'),
    
    # 4. Team Workspace 
    path('', include('team_registry.urls')),
    
    # 5. Features
    path('schedule/', include('scheduling.urls')),
    path('messages/', include('messagesapp.urls')),
    path('reports/', include('reports.urls')),
    # Felipe put you map here
]