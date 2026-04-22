
# Author: Mariam El-Mansouri Abaich
# ID: w2074138
# Contribution: Django Admin Registration for Messages Management (CWK2 Group Task)

from django.contrib import admin
from .models import Message, Team

admin.site.register(Message)

admin.site.register(Team)