from django.db import models

class FixVersion(models.Model):
    version = models.CharField(max_length=50)
    spec_path = models.CharField(max_length=200)

    def __str__(self):
        return version
