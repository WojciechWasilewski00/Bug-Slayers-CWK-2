# Author: Mariam El-Mansouri Abaich
# Student ID: w2074138
# Contribution: App configuration for Messages feature (CWK2)
from django.apps import AppConfig
# Import AppConfig class used to configure Django apps

class MessagesappConfig(AppConfig):
    # Defines configuration for the messagesapp application
    default_auto_field = 'django.db.models.BigAutoField'
    # Sets the default type for primary keys in models (auto-incrementing ID)
    name = 'messagesapp'
    # Specifies the name of the app so Django can recognise and register it