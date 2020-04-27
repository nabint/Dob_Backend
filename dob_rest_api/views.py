from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from dob_rest_api import serializers
from dob_rest_api import models


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiels"""
    serializer_class = serializers.UserProfileSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields=('name','email',)
    queryset = models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    
