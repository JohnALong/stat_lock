import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from statlockapp.models import Player, Match
from ..connection import Connection

@login_required
def match_details(request, match_id):

    if request.method == 'GET':
        match = Match.objects.get(id=match_id)
        print(match.won)
        # match = Match.objects.filter(player_id=player.id)
        # print(match, "stuff")
        
        players = match.player_set.all()
        for player in players:
            print(player.name, "stuff")
            print(player.eight_skill)

        template = 'matches/detail.html'
        context = {
            'match': match,
            'players': players
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data and form_data["actual_method"] == "PUT"
        ):
            match_won = form_data.get("won", False)
            match_to_update = Match.objects.get(pk=match_id)

            match_to_update.won = match_won
            match_to_update.match_type_id = form_data['matchtype']
            match_to_update.player_id = form_data['player']

            match_to_update.save()

            return redirect(reverse('statlockapp:team'))