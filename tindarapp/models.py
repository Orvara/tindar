from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

# Create your models here.
# Posts model.py


class Posts(models.Model):
    name = models.CharField(max_length = 60)
    subject = models.CharField(max_length = 255)
    from_email = models.CharField(max_length = 60)
    message = models.CharField(max_length = 10000)
    lesid = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' : ' +self.subject
