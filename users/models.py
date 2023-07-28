from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=250)
    profile_pic = models.CharField(max_length=100)
    birthdate = models.DateField()
    admin = models.BooleanField(default=False)
    role_options = [
        ("Scout", "Scout"),
        ("Parent", "Parent"),
        ("leader", "Leader"),
    ]
    role = models.CharField(choices=role_options, default="Scout")
    created = models.DateField(auto_now_add=True) # Will do a datetime.date.now() only 1 time when the row is created
    updated = models.DateField(auto_now=True) # Will do a datetime.date.now() every time a row is updated


class ScoutProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    scout_positions = [
        ("SPL", "Senior Patrol Leader"),
        ("ASPL", "Assistant Senior Patrol Leader"),
        ("PL", "Patrol Leader"),
        ("Bugler", "Bugler"),
        ("Troop Guide", "Troop Guide"),
        ("Quartermaster", "Quartermaster"),
        ("Troop Scribe", "Troop Scribe"),
        ("TOAR", "Troop Order of the Arrow Representative"),
        ("Troop Historian", "Troop Historian"),
        ("Instructor", "Instructor"),
        ("Chaplain Aide", "Chaplain Aide"),
        ("Den Chief", "Den Chief"),
        ("Webmaster", "Webmaster"),
        ("Webelos Deb Chief", "Webelos Deb Chief"),
        ("Outdoor Ethics Guide", "Outdoor Ethics Guide"),
        ("JA Scoutmaster", "Junior Assistant Scoutmaster"),
    ]
    position = models.CharField(choices=scout_positions)
    scout_ranks = [
        ("Scout", "Scout"),
        ("Tenderfoot", "Tenderfoot"),
        ("Second Class", "Second Class"),
        ("First Class", "First Class"),
        ("Star", "Star"),
        ("Life", "Life"),
        ("Eagle", "Eagle"),
    ]
    rank = models.CharField(choices=scout_ranks, default="Scout")
    # add in merit badge attribute once model is done
    # merit_badges = model.ManyToManyField(MeritBadge, on_delete=models.CASCADE)


class ParentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    # this will store the Parent's scouts/children
    children = models.ManyToManyField(User)


class LeaderProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    bsa_id = models.CharField(max_length=25)
    leader_positions = [
        ("Scoutmaster", "Scoutmaster"),
        ("Assistant Scoutmaster", "Assistant Scoutmaster"),
        ("Committee Chairman", "Committee Chairman"),
        ("Committee Member", "Committee Member"),
        ("Charter Organization Representative","Charter Organization Representative"),
    ]
    position = models.CharField(choices=leader_positions)
    # add in merit badge attribute once model is done
    # merit_badges = model.ManyToManyField(MeritBadge, on_delete=models.CASCADE)
