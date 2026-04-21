from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100, help_text="e.g. Bug Slayers Front End")
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Teams" #example code so that jayne can run scheduling page