from django.contrib import admin
from servicedesk.models import Incident
from servicedesk.models import Owner
from servicedesk.models import Elevator

# Register your models here.

admin.site.register(Incident)
admin.site.register(Owner)
admin.site.register(Elevator)
