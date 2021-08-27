from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class leaderboard(models.Model):
    username = models.CharField(_("username"), max_length=255)
    distance = models.IntegerField(_("distance"))
