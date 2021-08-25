from django.contrib import admin
from .models import WeeklyEvents, Tier, Challenge


admin.site.site_header = 'Adventure Runner Dashboard'
class WeeklyEventsAdmin(admin.ModelAdmin):
    list_display = ('event_date', 'tier', 'reward', 'Challenge', 'value')
    list_filter = ('event_date',)

# Register your models here.

admin.site.register(WeeklyEvents, WeeklyEventsAdmin)
admin.site.register(Tier)
admin.site.register(Challenge)


