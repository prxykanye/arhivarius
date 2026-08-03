from rest_framework import serializers
from .models import Channel


class ChannelCreateSerializer(serializers.Serializer):
    url = serializers.URLField()


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = "__all__"
