# Author: Mariam El-Mansouri Abaich
# Student ID: w2074138
# Contribution: Created the MessageForm to handle user input for sending messages

from django import forms
# Import Django forms module to create form classes
from .models import Message
# Import the Message model to link the form to the database
from team_registry.models import Team
# Import Team model so we can display team options in the form


class MessageForm(forms.ModelForm):
    # ModelForm automatically creates a form based on the Message model
    name = forms.CharField(required=True)
    # Additional field to capture sender name (not stored in model)
    email = forms.EmailField(required=True)
    # Additional field to capture sender email (not stored in model)

    class Meta:
        model = Message
        # Connects this form to the Message model
        fields = ['team', 'message_subject', 'message_content']
        # Defines which fields from the model will appear in the form

    def __init__(self, *args, **kwargs):
        # Override the default form initialisation
        super().__init__(*args, **kwargs)
        # Call parent constructor to initialise the form
        self.fields['team'].queryset = Team.objects.all()
        # Populate the team dropdown with all teams from the database
        self.fields['team'].empty_label = "Select Team"
        # Replace the default "------" with "Select Team" in the dropdown