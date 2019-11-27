# Serializers define the API representation.
from rest_framework import serializers

from .models import Profile


class ProfilesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['full_name', 'direct_tel', 'title', 'website', 'job_title', 'office_tel', 'avatar']
