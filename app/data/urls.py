from django.urls import path
from .views import ChannelCreateView

urlpatterns = [
    path("channels/create", ChannelCreateView.as_view()),
]
