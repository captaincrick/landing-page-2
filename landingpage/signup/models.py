from django.db import models
from django.core.urlresolvers import reverse


class SignUp(models.Model):

    name = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('signup:success')



# Create your models here.
