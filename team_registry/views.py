from django.shortcuts import render, get_object_or_404
from .models import Department, Team, TeamType, Dependency

def organisation_overview(request):
    departments = Department.objects.all()
    teams = Team.objects.all()
    return render(request, 'team_registry/organisation_overview.html', {
        'departments': departments,
        'teams': teams
    })

def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    teams = Team.objects.filter(department=department)
    return render(request, 'team_registry/department_detail.html', {
        'department': department,
        'teams': teams
    })

def team_detail(request, pk):
    team = get_object_or_404(Team, pk=pk)
    dependencies_from = Dependency.objects.filter(from_team=team)
    dependencies_to = Dependency.objects.filter(to_team=team)
    return render(request, 'team_registry/team_detail.html', {
        'team': team,
        'dependencies_from': dependencies_from,
        'dependencies_to': dependencies_to
    })