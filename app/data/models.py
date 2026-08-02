from django.db import models


class Channel(models.Model):
    class ChannelStatus(models.TextChoices):
        ACTIVE = "active", "Активен"
        INACTIVE = "inactive", "Не активен"

    id = models.AutoField(primary_key=True)
    url = models.URLField(unique=True)
    title = models.TextField()
    status = models.CharField(
        choices=ChannelStatus.choices,
        default=ChannelStatus.ACTIVE,
    )

    def __str__(self):
        return self.title
