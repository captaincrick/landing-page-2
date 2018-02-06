from django.db import models
from django.core.urlresolvers import reverse


class SignUp(models.Model):

    name = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField()
    wechat = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('signup_cn:success')



# Create your models here.
