from django.db import models

# Create your models here.
class MeritBadge(models.Model):
    name = models.CharField(max_length=150, blank=False)
    description = models.CharField(max_length=500, blank=False)
    eagle_required = models.BooleanField(default=False)
    logo_image = models.CharField(max_length=100)
