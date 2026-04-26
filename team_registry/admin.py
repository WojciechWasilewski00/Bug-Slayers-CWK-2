# Author: [Wojciech Wasileski]

# ID: [w2083613]

# Contribution: Backend Models for Team Management (CWK2)

from django.contrib import admin
from .models import Team, Skill, TeamDependency

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    # This controls what columns show up in the admin list
    list_display = ('team_name', 'department', 'manager')
    
    # This adds a search bar to the admin panel
    search_fields = ('team_name', 'department')
    
    # This adds a filter sidebar on the right
    list_filter = ('department', 'skills')
    
    # This makes the Many-to-Many skills selection much easier to use
    filter_horizontal = ('skills',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    search_fields = ('name',)