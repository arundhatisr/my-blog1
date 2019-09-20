
from django.conf import settings
from django.db import models
from django.utils import timezone


class Upload(models.Model):
    name = models.TextField()
    phone_no = models.CharField(max_length=10)
    address = models.TextField()
    locality = models.TextField()
    city = models.TextField()
    state = models.TextField()
    pincode = models.CharField(max_length=10)

    def Upload(self):

        self.save()

    def __str__(self):
        return self.name
