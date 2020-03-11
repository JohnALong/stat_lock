from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("team")
        verbose_name_plural = ("teams")

    def __str__(self):
        return self.name 