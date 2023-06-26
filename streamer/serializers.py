from rest_framework import serializers
from .models import Streamer


class StreamerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Streamer
        fields = '__all__'
