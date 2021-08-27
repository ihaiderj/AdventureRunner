from django.contrib import admin
from .models import leaderboard

# Register your models here.

class leaderboardAdmin(admin.ModelAdmin):
    list_display = ('username', 'distance',)

admin.site.register(leaderboard, leaderboardAdmin)
