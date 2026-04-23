from django.contrib import admin
from .models import TeamType, Department, Team, Dependency

@admin.register(TeamType)
class TeamTypeAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialisation', 'leader']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'team_type', 'created_at']

@admin.register(Dependency)
class DependencyAdmin(admin.ModelAdmin):
    list_display = ['from_team', 'to_team', 'dependency_type']