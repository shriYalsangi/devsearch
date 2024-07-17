from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
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

    subject = 'Welcome to DevSearch'
    message = 'We are happy to have you on board!'
    send_mail(
      subject,
      message,
      settings.EMAIL_HOST_USER,
      [profile.email],
      fail_silently=False,
    )


@receiver(post_save, sender=Profile)
def updateUser(sender, instance, created, **kwargs):
  profile = instance
  user = profile.user

  if created == False:
    user.username = profile.username
    user.email = profile.email
    user.first_name = profile.name
    user.save()


# post_save.connect(profileUpdated, sender=Profile)
# post_delete.connect(profileDeleted, sender=Profile) 