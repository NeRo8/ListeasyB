from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=30, blank=True)
    direct_tel = models.CharField(max_length=20, blank=True)
    title = models.CharField(max_length=30, blank=True)
    website = models.CharField(max_length=30, blank=True)
    job_title = models.CharField(max_length=30, blank=True)
    office_tel = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(upload_to='profile/', blank=True)

    def __str__(self):
        return self.full_name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()