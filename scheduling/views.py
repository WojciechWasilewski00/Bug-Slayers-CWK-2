from django.shortcuts import render
from .models import Meeting
from datetime import datetime, timedelta

def weekly_schedule(request):
    today = datetime.now().date()
    next_week = today + timedelta(days=7)
    
    # Fetch meetings happening in the next 7 days
    meetings = Meeting.objects.filter(
        meeting_date__range=[today, next_week]
    ).order_by('meeting_date', 'meeting_time')
    
    return render(request, 'scheduling/weekly.html', {'meetings': meetings})