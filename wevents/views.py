from django.shortcuts import render
from rest_framework import viewsets
from .models import WeeklyEvents, Tier, Challenge
from .serializers import WeeklyEventsSerializer, TierSerializer, ChallengeSerializer


class WeeklyEventsViewSet(viewsets.ModelViewSet):
    queryset = WeeklyEvents.objects.all()
    serializer_class = WeeklyEventsSerializer
class TierViewSet(viewsets.ModelViewSet):
    queryset = Tier.objects.all()
    serializer_class = TierSerializer
class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer