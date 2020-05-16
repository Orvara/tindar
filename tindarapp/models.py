from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

import misaka

# Create your models here.
# Posts model.py
from django.contrib.auth import get_user_model
User = get_user_model()
