from django.db import models

class Data(models.Model):
    name = models.CharField('Name of the data set', max_length=256)
    data = models.JSONField('JSON Data')

    def __str__(self) -> str:
        return self.name
