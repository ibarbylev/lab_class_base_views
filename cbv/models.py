from django.db import models


class PetForExample(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name
