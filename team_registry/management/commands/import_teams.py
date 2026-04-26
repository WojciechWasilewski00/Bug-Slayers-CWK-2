# AUTHOR: [Your Name]
# nCONTRIBUTORS: None (Individual Product)
# DESCRIPTION: A custom Django ETL engine that parses teams.csv. Implements a two-pass logic to handle Many-to-Many dependencies and skill mappings.

import csv
from django.core.management.base import BaseCommand
from team_registry.models import Team, TeamDependency, Skill

class Command(BaseCommand):
    help = "Import teams, skills, and dependencies from teams.csv"

    def handle(self, *args, **options):
        path = 'teams.csv'
        
        # We store dependencies to process in a second pass 
        # to ensure all teams exist before linking them.
        all_dependency_links = []

        with open(path, mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            # Clean headers to remove any accidental spaces
            reader.fieldnames = [name.strip() for name in reader.fieldnames]
            
            self.stdout.write(self.style.SUCCESS(f"Headers detected: {reader.fieldnames}"))

            for row in reader:
                name = row.get('Team Name', '').strip()
                if not name:
                    continue

                # 1. Update or Create the Team record
                # Map 'Development Focus Areas' to 'team_description'
                team, created = Team.objects.update_or_create(
                    team_name=name,
                    defaults={
                        'department': row.get('Department', '').strip(),
                        'team_lead_name': row.get('Team Leader', '').strip(),
                        'dept_head_name': row.get('Department Head', '').strip(),
                        'team_description': row.get('Development Focus Areas', '').strip(),
                        'dependency_type': row.get('Dependency Type', '').strip(),
                        'dependencies': row.get('Downstream Dependencies', '').strip(), 
                        'jira_board_link': row.get('Jira board Link', '').strip(),
                    }
                )

                # 2. Handle Skills (Many-to-Many)
                skills_str = row.get('Key Skills & Technologies', '')
                if skills_str:
                    # Split by comma, e.g. "Python, Java" -> ["Python", "Java"]
                    skill_names = [s.strip() for s in skills_str.split(',') if s.strip()]
                    for s_name in skill_names:
                        skill_obj, _ = Skill.objects.get_or_create(name=s_name)
                        team.skills.add(skill_obj)

                # 3. Queue Dependencies for the second pass
                raw_deps = row.get('Downstream Dependencies', '')
                if raw_deps:
                    dep_list = [d.strip() for d in raw_deps.split(',') if d.strip()]
                    for dep_name in dep_list:
                        all_dependency_links.append({
                            'from_team': team,
                            'to_team_name': dep_name
                        })

                self.stdout.write(f"{'Created' if created else 'Updated'}: {name}")

        # 4. Second Pass: Linking Team to Team
        self.stdout.write(self.style.WARNING("\nLinking team dependencies..."))
        for link in all_dependency_links:
            try:
                target_team = Team.objects.get(team_name=link['to_team_name'])
                # Create relationship in the 'through' table
                TeamDependency.objects.get_or_create(
                    from_team=link['from_team'],
                    to_team=target_team,
                    defaults={'dependency_type': 'downstream'} 
                )
                self.stdout.write(f"  Link: {link['from_team']} -> {target_team}")
            except Team.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"  Skipped: Dependency '{link['to_team_name']}' not found in database."))

        self.stdout.write(self.style.SUCCESS("\nData import successful!"))