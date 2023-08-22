from rest_framework import serializers
from .models import Entry, UserProfile

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['user', 'date', 'content']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user']