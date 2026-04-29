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
    dept_head_name = models.CharField(max_length=255, blank=True, null=True)
    team_lead_name = models.CharField(max_length=255, blank=True, null=True)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='managed_teams')
    dependencies = models.TextField(blank=True) 
    dependency_type = models.CharField(max_length=100, blank=True, null=True)
    skills = models.ManyToManyField('Skill', blank=True)
    jira_board_link = models.URLField(max_length=500, blank=True, null=True)
    depends_on = models.ManyToManyField(
        'self', 
        through='TeamDependency', 
        symmetrical=False, 
        related_name='required_by'
    )
    
    def __str__(self):
        return self.team_name

class TeamDependency(models.Model):
    TYPES = (
        ('upstream', 'Upstream'),
        ('downstream', 'Downstream'),
    )
    from_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='dependency_source')
    to_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='dependency_target')
    dependency_type = models.CharField(max_length=20, choices=TYPES, default='upstream')

    