
from django.shortcuts import render
from django.http import HttpResponse
from team_registry.models import Team
import csv

# PDF imports
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib import colors


def reports_dashboard(request):
    query = request.GET.get('search')

    teams = Team.objects.all()

    if query:
        teams = teams.filter(team_name__icontains=query)

    total_teams = teams.count()

    return render(request, 'reports.html', {
        'teams': teams,
        'total_teams': total_teams,
        'query': query
    })

# 🔹 Reports Dashboard
def reports_dashboard(request):
    teams = Team.objects.all()
    total_teams = teams.count()

    # You don’t have manager field yet
    teams_without_managers = 0

    return render(request, 'reports.html', {
        'teams': teams,
        'total_teams': total_teams,
        'teams_without_managers': teams_without_managers
    })


# 🔹 Export Excel (CSV)
def export_excel(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="report.csv"'

    writer = csv.writer(response)
    writer.writerow(['Team'])

    for team in Team.objects.all():
        writer.writerow([team.team_name])

    return response


# 🔹 Export PDF
def export_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    doc = SimpleDocTemplate(response)

    data = [['Team']]

    for team in Team.objects.all():
        data.append([team.team_name])

    table = Table(data)

    doc.build([table])

    return response
