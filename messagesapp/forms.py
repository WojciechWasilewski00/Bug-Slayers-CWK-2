from django import forms
from .models import Message
from teamapp.models import Team


class MessageForm(forms.ModelForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = Message
        fields = ['team', 'message_subject', 'message_content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['team'].queryset = Team.objects.all()