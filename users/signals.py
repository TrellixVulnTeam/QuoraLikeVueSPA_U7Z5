from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver

from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_authentication_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)

# @receiver(post_save, sender=PersoUser)
# def create_Profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=PersoUser)
# def save_Profile(sender, instance, **kwargs):
#     instance.profile.save()
