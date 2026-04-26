# Author: Mariam El-Mansouri Abaich
# Student ID: w2074138
# Contribution: URL routing for Messages feature (CWK2)

from django.urls import path
# Import path function to define URL patterns
from . import views
# Import views file to connect URLs to backend functions


urlpatterns = [
    # Default route → loads inbox page
    path('', views.inbox, name='inbox'),
    # Route for creating a new message
    path('new-message/', views.new_message, name='new_message'),
    # Route for viewing sent messages
    path('sent/', views.sent, name='sent'),
    # Route for viewing draft messages
    path('drafts/', views.drafts, name='drafts'),
    # messagesapp/urls.py
]