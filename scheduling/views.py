from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Meeting
from .forms import MeetingForm

# 1. The Weekly List View (Read)
from django.utils import timezone

def weekly_schedule(request):
    # Only get meetings where the date is today or in the future
    meetings = Meeting.objects.filter(date_time__gte=timezone.now()).order_by('date_time')
    form = MeetingForm()
    return render(request, 'scheduling/weekly.html', {'meetings': meetings, 'form': form})
    
# 2. The Form View (Create)
def schedule_meeting(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('weekly_schedule') # Redirects back to the table
    return redirect('weekly_schedule') # Fallback

# 3. The Detail View (Read single item)
def meeting_detail(request, pk):
    # Look for a specific meeting by its ID, or return 404 error if not found
    meeting = get_object_or_404(Meeting, pk=pk)
    return render(request, 'scheduling/meeting_detail.html', {'meeting': meeting})

# 4. The Delete View (Delete)
def delete_meeting(request, pk):
    meeting = get_object_or_404(Meeting, pk=pk)
    if request.method == 'POST':
        meeting.delete()
        return redirect('weekly_schedule')
    
    return render(request, 'scheduling/confirm_delete.html', {'meeting': meeting})

    # Edit an existing meeting
def edit_meeting(request, pk):
    meeting = get_object_or_404(Meeting, pk=pk)
    if request.method == 'POST':
        # 'instance=meeting' tells Django to update this specific record
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect('weekly_schedule')
    else:
        form = MeetingForm(instance=meeting)
    
    return render(request, 'scheduling/schedule_form.html', {
        'form': form,
        'edit_mode': True  # This helps us change the button text in the HTML
    })