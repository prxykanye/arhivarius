from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from data.models import Channel
from data.serializers import ChannelSerializer

# Create your views here.


@api_view(["GET", "POST"])
def channels_view(request: Request):

    if request.method == "GET":

        channels = Channel.objects.all()
        serializer = ChannelSerializer(channels, many=True)
        return Response(serializer.data)

    elif request.method == "POST":

        serializer = ChannelSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return None
