from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Lecture(models.Model):
    name = models.CharField(max_length=100, null=True)
    number = models.IntegerField(null=True)
    fresh_suguni = models.IntegerField(null=True)
    fresh_sugang = models.IntegerField(null=True)
    fresh_limit = models.IntegerField(null=True)
    sopho_suguni = models.IntegerField(null=True)
    sopho_sugang = models.IntegerField(null=True)
    sopho_limit = models.IntegerField(null=True)
    junior_suguni = models.IntegerField(null=True)
    junior_sugang = models.IntegerField(null=True)
    junior_limit = models.IntegerField(null=True)
    senior_suguni = models.IntegerField(null=True)
    senior_sugang = models.IntegerField(null=True)
    senior_limit = models.IntegerField(null=True)

    def __str__(self):
        return str(self.name)
       
