from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(models.Model):
    name = models.CharField(max_length=200, unique=True)
    vote_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Party(models.Model):
    party_name = models.CharField(max_length=100)
    voter = models.ForeignKey(User, on_delete=models.SET_NULL)

    def __str__(self):
        return self.party_name

    @receiver(post_save, sender=User)
    def notify_new_vote(self, sender, instance, created, **kwargs):
        if created:
            print('{} created'.format(instance.name))
