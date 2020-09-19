from django.contrib.postgres.fields import HStoreField
from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField('Name of the data set', max_length=256)
    data = models.JSONField('JSON Data')
