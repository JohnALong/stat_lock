from django.db import models

class MatchType(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("matchtype")
        verbose_name_plural = ("matchtypes")

    def __str__(self):
        return self.name