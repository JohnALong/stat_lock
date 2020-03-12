from django.db import models
from django.db.models import F

class Player(models.Model):

    name = models.CharField(max_length=50)
    eight_rating = models.IntegerField(default=0)
    nine_rating = models.IntegerField(default=0)
    team = models.ForeignKey('team', on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("player")
        verbose_name_plural = ("players")

    def __str__(self):
        return f' {self.name} is a {self.eight_rating} in 8 ball and a {self.nine_rating} in 9 ball'