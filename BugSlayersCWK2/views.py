#jayne
from django.shortcuts import render, redirect

# This handles the root URL (127.0.0.1:8000/)
def home_redirect(request):
    return redirect('dashboard')

# This handles the dashboard URL (127.0.0.1:8000/dashboard/)
def dashboard_view(request):
    return render(request, 'dashboard.html')