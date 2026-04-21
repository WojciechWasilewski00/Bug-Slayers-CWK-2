from django.urls import path
from . import views

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
    path('new-message/', views.new_message, name='new_message'),
    path('sent/', views.sent, name='sent'),
    path('drafts/', views.drafts, name='drafts'),
]