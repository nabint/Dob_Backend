from rest_framework import serializers
from dob_rest_api import models

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user Profile object"""
    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','phoneNo','password')
        extra_kwargs={
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }

    def create(self,validated_data):
        """Create and return new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password'],
            phoneNo=validated_data['phoneNo']
        )

        return user
