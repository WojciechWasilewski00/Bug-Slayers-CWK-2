from django.shortcuts import render, get_object_or_404, redirect
from .models import Department, Team, TeamType, Dependency
from .forms import DepartmentForm, TeamForm, TeamTypeForm, DependencyForm

# --- Organisation Overview ---
def organisation_overview(request):
    departments = Department.objects.all()
    teams = Team.objects.all()
    return render(request, 'team_registry/organisation_overview.html', {
        'departments': departments,
        'teams': teams
    })

# --- Department CRUD ---
def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    teams = Team.objects.filter(department=department)
    return render(request, 'team_registry/department_detail.html', {
        'department': department,
        'teams': teams
    })

def department_create(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('organisation_overview')
    return render(request, 'team_registry/department_form.html', {'form': form, 'title': 'Add Department'})

def department_edit(request, pk):
    department = get_object_or_404(Department, pk=pk)
    form = DepartmentForm(request.POST or None, instance=department)
    if form.is_valid():
        form.save()
        return redirect('department_detail', pk=pk)
    return render(request, 'team_registry/department_form.html', {'form': form, 'title': 'Edit Department'})

def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('organisation_overview')
    return render(request, 'team_registry/confirm_delete.html', {'object': department, 'type': 'Department'})

# --- Team CRUD ---
def team_detail(request, pk):
    team = get_object_or_404(Team, pk=pk)
    dependencies_from = Dependency.objects.filter(from_team=team)
    dependencies_to = Dependency.objects.filter(to_team=team)
    return render(request, 'team_registry/team_detail.html', {
        'team': team,
        'dependencies_from': dependencies_from,
        'dependencies_to': dependencies_to
    })

def team_create(request):
    form = TeamForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('organisation_overview')
    return render(request, 'team_registry/team_form.html', {'form': form, 'title': 'Add Team'})

def team_edit(request, pk):
    team = get_object_or_404(Team, pk=pk)
    form = TeamForm(request.POST or None, instance=team)
    if form.is_valid():
        form.save()
        return redirect('team_detail', pk=pk)
    return render(request, 'team_registry/team_form.html', {'form': form, 'title': 'Edit Team'})

def team_delete(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        team.delete()
        return redirect('organisation_overview')
    return render(request, 'team_registry/confirm_delete.html', {'object': team, 'type': 'Team'})

# --- TeamType CRUD ---
def teamtype_list(request):
    teamtypes = TeamType.objects.all()
    return render(request, 'team_registry/teamtype_list.html', {'teamtypes': teamtypes})

def teamtype_create(request):
    form = TeamTypeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('teamtype_list')
    return render(request, 'team_registry/teamtype_form.html', {'form': form, 'title': 'Add Team Type'})

def teamtype_edit(request, pk):
    teamtype = get_object_or_404(TeamType, pk=pk)
    form = TeamTypeForm(request.POST or None, instance=teamtype)
    if form.is_valid():
        form.save()
        return redirect('teamtype_list')
    return render(request, 'team_registry/teamtype_form.html', {'form': form, 'title': 'Edit Team Type'})

def teamtype_delete(request, pk):
    teamtype = get_object_or_404(TeamType, pk=pk)
    if request.method == 'POST':
        teamtype.delete()
        return redirect('teamtype_list')
    return render(request, 'team_registry/confirm_delete.html', {'object': teamtype, 'type': 'Team Type'})

# --- Dependency CRUD ---
def dependency_list(request):
    dependencies = Dependency.objects.all()
    return render(request, 'team_registry/dependency_list.html', {'dependencies': dependencies})

def dependency_create(request):
    form = DependencyForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dependency_list')
    return render(request, 'team_registry/dependency_form.html', {'form': form, 'title': 'Add Dependency'})

def dependency_edit(request, pk):
    dependency = get_object_or_404(Dependency, pk=pk)
    form = DependencyForm(request.POST or None, instance=dependency)
    if form.is_valid():
        form.save()
        return redirect('dependency_list')
    return render(request, 'team_registry/dependency_form.html', {'form': form, 'title': 'Edit Dependency'})

def dependency_delete(request, pk):
    dependency = get_object_or_404(Dependency, pk=pk)
    if request.method == 'POST':
        dependency.delete()
        return redirect('dependency_list')
    return render(request, 'team_registry/confirm_delete.html', {'object': dependency, 'type': 'Dependency'})