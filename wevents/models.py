from django.db import models

class Tier(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name 

class Challenge(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name 

class WeeklyEvents(models.Model):
    event_date = models.DateField()
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE, related_name='tier')
    reward = models.CharField(max_length=30)
    Challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE , related_name= 'challenge')
    value = models.CharField(max_length=30, default="")
       
    # class Meta:1
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    # def __str__(self):
    #     return self.reward

# class leaderboard(models.Model):
#     user_name = models.CharField(max_length = 30, unique=True)
#     distance = models.IntegerField()
