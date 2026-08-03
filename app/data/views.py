from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from data.models import Channel
from data.serializers import ChannelCreateSerializer
from .services.youtube import get_channel_info


# Create your views here.
class ChannelCreateView(APIView):
    def post(self, request: Request, *args, **kwargs):
        serializer = ChannelCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = get_channel_info(serializer.validated_data["url"])

        channel, created = Channel.objects.update_or_create(
            url=data["url"],
            channel_id=data["channel_id"],
            title=data["title"],
            status=data["status"],
        )

        return Response(
            data,
            status=status.HTTP_201_CREATED,
        )
