import csv
import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from teamapp.models import Team, Skill

class Command(BaseCommand):
    help = 'Imports teams with dependency types'

    def handle(self, *args, **kwargs):
        file_path = 'teams.csv'
        try:
            with open(file_path, mode='r', encoding='latin-1') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    leader_name = row.get('Team Leader') or 'Staff_Member'
                    username = leader_name.replace(" ", "_").lower()
                    manager, _ = User.objects.get_or_create(
                        username=username, defaults={'first_name': leader_name}
                    )

                    team, _ = Team.objects.update_or_create(
                        team_name=row.get('Team Name'),
                        defaults={
                            'department': row.get('Department'),
                            'team_description': row.get('Development Focus Areas'),
                            'dependencies': row.get('Downstream Dependencies'),
                            'dependency_type': row.get('Dependency Type'), # New mapping
                            'manager': manager
                        }
                    )

                    skills_raw = row.get('Key Skills & Technologies') or ''
                    if skills_raw:
                        for s_name in [s.strip() for s in skills_raw.split(',') if s.strip()]:
                            skill_obj, _ = Skill.objects.get_or_create(name=s_name)
                            team.skills.add(skill_obj)

                    self.stdout.write(self.style.SUCCESS(f'Imported: {team.team_name}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))