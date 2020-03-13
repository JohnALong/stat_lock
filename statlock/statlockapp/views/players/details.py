import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from statlockapp.models import Player
from ..connection import Connection

@login_required
def player_details(request, player_id):

    if request.method == 'GET':
        player = Player.objects.get(id=player_id)

        template = 'players/detail.html'
        context = {
            'player': player
        }

        return render(request, template, context)

    if request.method == 'POST':
        form_data = request.POST
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            player = Player.objects.get(id=player_id)
            player.delete()

            return redirect(reverse('statlockapp:team'))