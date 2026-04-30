from django.shortcuts import render, redirect, get_object_or_404, redirect
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
    
def meeting_details(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    return render(request, 'scheduling/meeting_details.html', {'meeting': meeting})

def edit_meeting(request, meeting_id): # Match the URL variable name
    meeting = get_object_or_404(Meeting, id=meeting_id)
    if request.method == 'POST':
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect('scheduling:weekly_schedule')
    else:
        form = MeetingForm(instance=meeting)
    return render(request, 'scheduling/schedule_form.html', {'form': form, 'edit_mode': True})

def delete_meeting(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    if request.method == "POST":
        meeting.delete()
    return redirect('scheduling:weekly_schedule')