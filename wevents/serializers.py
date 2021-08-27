from rest_framework import serializers
from .models import WeeklyEvents, Tier, Challenge



class WeeklyEventsSerializer(serializers.ModelSerializer):
    tier = serializers.CharField(source='tier.name')
    Challenge = serializers.CharField(source='Challenge.name')
    class Meta:
        model = WeeklyEvents
        fields= ('event_date', 'tier', 'reward', 'Challenge', 'value')

class TierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tier
        fields= ('name',)
class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields= ('name',)
# class leaderboardSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = leaderboard
#         fields= ('user_name', 'distance')