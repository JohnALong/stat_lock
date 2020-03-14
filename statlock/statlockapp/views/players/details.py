import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from statlockapp.models import Player, Match
from ..connection import Connection

@login_required
def player_details(request, player_id):

    if request.method == 'GET':
        player = Player.objects.get(id=player_id)
        print(player.name)
        # match = Match.objects.filter(player_id=player.id)
        # print(match, "stuff")
        
        matches = player.match_set.all()
        for match in matches:
            print(match.match_type, "stuff")
            print(match.won)
            print(match.date)

        template = 'players/detail.html'
        context = {
            'player': player,
            'matches': matches
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data and form_data["actual_method"] == "PUT"
        ):

            player_to_update = Player.objects.get(pk=player_id)

            player_to_update.name = form_data['name']
            player_to_update.eight_rating = form_data['eight_rating']
            player_to_update.nine_rating = form_data['nine_rating']
            player_to_update.team_id = request.user.captain.team_id

            player_to_update.save()

            return redirect(reverse('statlockapp:team'))


    if request.method == 'POST':
        form_data = request.POST
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            player = Player.objects.get(id=player_id)
            player.delete()

            return redirect(reverse('statlockapp:team'))