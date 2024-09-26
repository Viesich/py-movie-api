from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)
    duration = models.IntegerField()

    def __str__(self) -> str:
        return str(self.title)
