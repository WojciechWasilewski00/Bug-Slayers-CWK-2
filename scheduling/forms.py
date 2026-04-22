from django import forms
from .models import Meeting

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['team', 'subject', 'description', 'date_time', 'platform']
        # This widget makes the date/time field show a calendar picker
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'team': forms.Select(attrs={'class': 'form-select'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'platform': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Zoom, Teams'}),
        }