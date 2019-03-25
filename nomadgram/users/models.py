from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

class User(AbstractUser):

    GENDER_CHOICES = (
        ('male','Male'),
        ('female', 'Female'),
        ('not-specified','Not specified')
    )

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    wesite = models.URLField(null=True)
    bio = models.TextField(null=True)
    phone = models.CharField(max_length=140, null=True)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("userdirs:detail", kwargs={"username": self.username})
