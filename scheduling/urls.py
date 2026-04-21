from django.urls import path
from . import views

urlpatterns = [
    # This makes the page available at /scheduling/
    path('', views.weekly_schedule, name='weekly_schedule'),
]