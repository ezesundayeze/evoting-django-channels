from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class User(models.Model):
    name = models.CharField(max_length=200, unique=True)
    vote_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Party(models.Model):
    party_name = models.CharField(max_length=100)

    def __str__(self):
        return self.party_name


class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)

    @receiver(post_save, sender=User)
    def notify_new_vote(sender, instance, created, **kwargs):
        if created:
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "notify_voters", {
                    "type": "user.vote",
                    "event": "new vote",
                    "name": instance.name
                }
            )
