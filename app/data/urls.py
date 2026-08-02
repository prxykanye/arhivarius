from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import channels_view

urlpatterns = [
    path("channels/", channels_view),
]

urlpatterns = format_suffix_patterns(urlpatterns)
