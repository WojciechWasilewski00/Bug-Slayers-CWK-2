# Author: Mariam El-Mansouri Abaich
# ID: w2074138
# Contribution: Django Admin Registration for Messages Management (CWK2 Group Task)

from django.contrib import admin
# Import Django admin module to manage models via the admin interface
from .models import Message
# Import the Message model that was created for the messaging system
admin.site.register(Message)
# Register the Message model in the admin panel
# This allows admin users to:
# - View all messages
# - Add new messages
# - Edit existing messages
# - Delete messages