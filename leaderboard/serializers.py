from rest_framework import serializers
from .models import leaderboard



class leaderboardSerializers(serializers.ModelSerializer):
    class Meta:
        model = leaderboard
        fields = [
            'username', 
            'distance',
            ]