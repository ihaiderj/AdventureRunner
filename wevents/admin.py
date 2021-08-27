from django.contrib import admin
from .models import WeeklyEvents, Tier, Challenge


admin.site.site_header = 'Adventure Runner Dashboard'
class WeeklyEventsAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_date', 'tier', 'reward', 'Challenge', 'value')
    list_filter = ('event_date',)
# class leaderboardAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user_name', 'distance', )
#     sort_by = ('distance')

# Register your models here.

admin.site.register(WeeklyEvents, WeeklyEventsAdmin)
admin.site.register(Tier)
admin.site.register(Challenge)
# admin.site.register(leaderboard,leaderboardAdmin)


