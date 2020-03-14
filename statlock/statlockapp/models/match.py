from django.db import models
from .matchtype import MatchType
from .player import Player

class Match(models.Model):

    date = models.DateField(auto_now=False, auto_now_add=True)
    won = models.BooleanField()
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match_type = models.ForeignKey(MatchType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("match")
        verbose_name_plural = ("matches")

    # def __str__(self):
    #     return self.date