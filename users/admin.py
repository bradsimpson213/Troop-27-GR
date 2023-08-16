from django.contrib import admin
from .models import UserProfile, ScoutProfile, ParentProfile, LeaderProfile


# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ScoutProfile)
admin.site.register(ParentProfile)
admin.site.register(LeaderProfile)
