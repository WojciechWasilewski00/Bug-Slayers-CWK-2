from django.shortcuts import render, get_object_or_404
from django.db.models import Q  # This allows for "OR" searches
from team_registry.models import Team
from .models import Team, TeamDependency, Skill

def team_page(request):
    # Get the text from the search bar (name="search" in HTML)
    query = request.GET.get('search')
    
    if query:
        # Filter by Name OR Department OR Description (case-insensitive)
        teams = Team.objects.filter(
            Q(team_name__icontains=query) | 
            Q(department__icontains=query) |
            Q(team_description__icontains=query)
        ).distinct()
    else:
        teams = Team.objects.all()
        
    return render(request, 'team_page.html', {'teams': teams, 'query': query})

def team_detail(request, pk):
    team = get_object_or_404(Team, pk=pk)
    dependencies = TeamDependency.objects.filter(from_team=team).select_related('to_team')
    skills_list = team.skills.all() 
    
    return render(request, 'team_detail.html', {
        'team': team, 
        'skills': skills_list,
        'dependencies': dependencies,
    })