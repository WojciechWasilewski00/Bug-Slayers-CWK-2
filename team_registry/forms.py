from django import forms
from .models import Department, Team, TeamType, Dependency

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'specialisation', 'leader']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'description', 'department', 'team_type']

class TeamTypeForm(forms.ModelForm):
    class Meta:
        model = TeamType
        fields = ['name']

class DependencyForm(forms.ModelForm):
    class Meta:
        model = Dependency
        fields = ['from_team', 'to_team', 'dependency_type', 'description']