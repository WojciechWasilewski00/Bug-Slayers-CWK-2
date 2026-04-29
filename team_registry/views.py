from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Team, TeamDependency, Skill
import json

def team_page(request):
    query = request.GET.get('search')
    if query:
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
    nodes = [{'id': team.pk, 'name': team.team_name, 'type': 'main'}]
    links = []
    for dep in dependencies:
        nodes.append({'id': dep.to_team.pk, 'name': dep.to_team.team_name, 'type': dep.dependency_type})
        links.append({'source': team.pk, 'target': dep.to_team.pk, 'type': dep.dependency_type})
    graph_data = json.dumps({'nodes': nodes, 'links': links})
    return render(request, 'team_detail.html', {
        'team': team,
        'skills': skills_list,
        'dependencies': dependencies,
        'graph_data': graph_data,
    })

def organisation(request):
    all_teams = Team.objects.all().order_by('department', 'team_name')
    departments = {}
    for team in all_teams:
        dept = team.department or 'Unassigned'
        if dept not in departments:
            departments[dept] = []
        departments[dept].append(team)
    all_dependencies = TeamDependency.objects.select_related('from_team', 'to_team').all()
    return render(request, 'organisation.html', {
        'departments': departments,
        'all_dependencies': all_dependencies,
    })
