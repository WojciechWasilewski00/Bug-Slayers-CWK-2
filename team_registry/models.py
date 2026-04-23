from django.db import models
from django.contrib.auth.models import User

# Author: [Wojciech Wasileski]

# ID: [w2083613]

# Contribution: Backend Models for Team Management (CWK2)

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    team_name = models.CharField(max_length=255)
    department = models.CharField(max_length=255, blank=True, null=True)
    team_description = models.TextField(blank=True)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='managed_teams')
    dependencies = models.TextField(blank=True)      # The "Downstream Dependencies" column
    dependency_type = models.CharField(max_length=255, blank=True, null=True) # The "Dependency Type" column
    
    # This single line handles the relationship for both Team and Skill
    skills = models.ManyToManyField(Skill, related_name='teams')

    def __str__(self):
        return self.team_name