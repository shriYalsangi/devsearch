from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=Profile)
def profileUpdated(sender, instance, created, **kwargs):
  print('Profile Updated:', instance, created)

@receiver(post_delete, sender=Profile)
def profileDeleted(sender, instance, **kwargs):
  user = instance.user
  user.delete()
  print('Profile Deleted:', instance)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
  if created:
    user = instance
    profile = Profile(user=user, username=user.username, email=user.email, name=user.first_name)
    profile.save()




# post_save.connect(profileUpdated, sender=Profile)
# post_delete.connect(profileDeleted, sender=Profile) 