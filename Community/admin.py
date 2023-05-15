from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Citizen)
admin.site.register(Community)
admin.site.register(Member)
admin.site.register(CommunityLeader)
admin.site.register(Household)
admin.site.register(Housemember)

