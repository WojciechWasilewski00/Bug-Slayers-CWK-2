Error Type,
What Happened,
Technical Solution

AttributeError,"The URL was looking for weekly_schedule or schedule_meeting, but the functions were missing or misspelled in views.py.",Alignment: Audited views.py to ensure function names matched the urls.py strings exactly

NameError,Tried to use timezone.now() without importing the timezone utility from django.utils.,Dependency Management: Added the missing import statement at the top of the file to provide the necessary context to Python.

NoReverseMatch,Django crashed while trying to build a link for meeting_detail because the meeting.pk variable was empty.,Context Correction: Identified that the link was placed in the <thead> (header) where the loop variable didn't exist. Moved the code into the <tbody> loop.

Template Logic Error,Buttons for View/Edit/Delete weren't appearing or were causing errors on the frontend.,CRUD Implementation: Mapped Primary Keys (pk) from the database objects to the template URL tags to allow row-specific actions.


How to phrase this for your Report
When you move these to your final assignment, use professional language like this:

"During the development of the Scheduling module, I adopted an iterative debugging approach. For instance, when encountering a NoReverseMatch error, I analyzed the Django traceback to identify a scope issue within the template. By moving the URL resolution logic inside the logic-based for-loop, I ensured that the Primary Key was correctly passed to the URL resolver. This refined my understanding of how Django maps database records to frontend templates."

Feature,Your Current base.html,Benefit

Styling,CSS Custom Variables (:root),Easy to maintain and update brand colors.

Logic,request.resolver_match,User always knows their location in the app.

UX,Sidebar Modal Trigger,"Allows meeting creation from any page, improving workflow speed."

Visuals,Plus Jakarta Sans + Floating Nav,"Achieves a ""Premium"" SaaS (Software as a Service) look."