from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = Message
        fields = ['team', 'message_subject', 'message_content']