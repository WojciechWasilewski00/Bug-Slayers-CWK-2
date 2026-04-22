from django.db import models

class Meeting(models.Model):
    # Ensure all lines below are aligned with EXACTLY 4 spaces or 1 tab
    team = models.ForeignKey('team_registry.Team', on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    description = models.TextField()
    date_time = models.DateTimeField()
    platform = models.CharField(max_length=100)

    def __str__(self):
        return self.subject