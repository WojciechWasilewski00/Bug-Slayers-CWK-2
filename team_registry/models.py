from django.db import models
from django.contrib.auth.models import User

class TeamType(models.Model):
    name = models.CharField(max_length=100, help_text="e.g. Frontend, Backend, QA")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Team Types"


class Department(models.Model):
    name = models.CharField(max_length=100, help_text="e.g. Engineering, Design")
    specialisation = models.CharField(max_length=200, blank=True, null=True)
    leader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='led_departments')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Departments"


class Team(models.Model):
    name = models.CharField(max_length=100, help_text="e.g. Bug Slayers Front End")
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='teams')
    team_type = models.ForeignKey(TeamType, on_delete=models.SET_NULL, null=True, blank=True, related_name='teams')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Teams"


class Dependency(models.Model):
    DEPENDENCY_TYPES = [
        ('upstream', 'Upstream'),
        ('downstream', 'Downstream'),
    ]
    from_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='dependencies_from')
    to_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='dependencies_to')
    dependency_type = models.CharField(max_length=20, choices=DEPENDENCY_TYPES)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.from_team} → {self.to_team} ({self.dependency_type})"

    class Meta:
        verbose_name_plural = "Dependencies"