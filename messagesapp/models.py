# Author: Mariam El-Mansouri Abaich
# ID: w2074138
# Contribution: Backend Models for Messages Management (CWK2)

from django.db import models
# Import Django models module to define database tables
from django.contrib.auth.models import User
# Import built-in User model for authentication (sender of messages)


class Message(models.Model):
    # Defines the Message model (database table)
    message_subject = models.CharField(max_length=255)
    # Stores the subject/title of the message (short text)
    message_content = models.TextField()
    # Stores the main content/body of the message (long text)
    message_status = models.CharField(max_length=10)
    # Stores the status of the message (e.g. 'draft', 'sent', 'read')
    sent_date = models.DateTimeField(auto_now_add=True)
    # Automatically stores the date and time when the message is created
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    # Links the message to a user (who sent it)
    # If the user is deleted, their messages are also deleted
    team = models.ForeignKey('team_registry.Team', on_delete=models.CASCADE)
    # Links the message to a specific team from the team_registry app
    # This allows messages to be associated with teams

    def __str__(self):
        # Defines how the message is displayed in the admin panel
        return self.message_subject
    