from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import leaderboardSerializers
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F
from rest_framework.decorators import permission_classes
from rest_framework import permissions

from .models import leaderboard

# Create your views here.

class UpdateLeaderboard(APIView):
    
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get','post']

    def get(self, request, *args, **kwargs):
        serializer = leaderboardSerializers(leaderboard.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format = None):
              
        serializer = leaderboardSerializers(data=request.data)
        if serializer.is_valid():
            username, distance = serializer.validated_data
            # if leaderboard.objects.filter(username).exists():
            #     serializer = leaderboard.objects.get(username)
            #     serializer.distance = F('distance') + distance  
            serializer.save()
            
        return Response(None, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Leaderboard(APIView):    
    def get(self, request, formate=None, **kwargs):
        scores = leaderboard.objects.all().order_by('-distance')[:10]
        serializer = leaderboardSerializers(scores, many=True)
        return Response(serializer.data)
            
            
                
                
