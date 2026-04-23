from django.urls import path, include
from . import views

urlpatterns = [
    # Removing the 'schedule/' prefix here because we added it in the main urls.py
    path('schedule/', views.weekly_schedule, name='weekly_schedule'),
    path('create/', views.schedule_meeting, name='schedule_meeting'),
    path('meeting/<int:pk>/', views.meeting_detail, name='meeting_detail'),
    path('meeting/<int:pk>/edit/', views.edit_meeting, name='edit_meeting'),
    path('meeting/<int:pk>/delete/', views.delete_meeting, name='delete_meeting'),
    path('accounts/', include('django.contrib.auth.urls')),
]