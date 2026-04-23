# Author: Mariam El-Mansouri Abaich
# ID: w2074138
# Contribution: Backend Models for Messages Management (CWK2)

from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    message_subject = models.CharField(max_length=255)
    message_content = models.TextField()
    message_status = models.CharField(max_length=10)  # draft / sent / read
    sent_date = models.DateTimeField(auto_now_add=True)

    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey('team_registry.Team', on_delete=models.CASCADE)

    def __str__(self):
        return self.message_subject

