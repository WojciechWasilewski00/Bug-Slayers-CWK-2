from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Meeting
from .forms import MeetingForm
from django.contrib.auth.decorators import login_required
from team_registry.models import Team
# 1. The Dashboard View
def dashboard(request):
    # This renders your dashboard.html
    return render(request, 'scheduling/dashboard.html')

# 2. The Add Meeting View (for your button)
def create_meeting(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('scheduling:weekly_schedule')
    else:
        form = MeetingForm()
    return render(request, 'scheduling/schedule_form.html', {'form': form})

# 3. Add placeholders for your other URLs so they don't crash
def weekly_schedule(request):
    meetings = Meeting.objects.all().order_by('date_time')
    teams = Team.objects.all()
    return render(request, 'scheduling/weekly_schedule.html', {
        'meetings': meetings,
        'teams': teams,
    })
    
def meeting_detail(request, pk):
    return render(request, 'scheduling/meeting_detail.html')

def edit_meeting(request, pk):
    return render(request, 'scheduling/edit_form.html')

def delete_meeting(request, pk):
    return render(request, 'scheduling/delete_confirm.html')