import sqlite3
from django.urls import reverse
from django.db.models import Count, F
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from statlockapp.models import Player, Match
from ..connection import Connection

@login_required
def player_details(request, player_id):

    if request.method == 'GET':
        # single player being pulled for details
        player = Player.objects.get(id=player_id)
        # print(player.name)

        # getting # of matches to be used for win percentage
        nine_count = player.match_set.filter(match_type=2).order_by('-id')[:20].count()
        # print("count", nine_count)
        # pull most recent 20 9 ball matches
        nine_matches = player.match_set.filter(match_type=2).order_by('-id')[:20]
        # calculate win percentage
        nine_wins = 0
        nine_percentage = 0
        for nine_match in nine_matches:
            if nine_match.won==True:
                nine_wins += 1
                # print("9", nine_match.won)
        try:        
            nine_percentage = (nine_wins/nine_count)*100
        except ZeroDivisionError:
            nine_percentage = 0

        # get count for division used in win percentage
        eight_count = player.match_set.filter(match_type=1).order_by('-id')[:20].count()
        # print("count", eight_count)
        # pull most recent 20 8 ball matches
        eight_matches = player.match_set.filter(match_type=1).order_by('-id')[:20]
        # calculate win percentage
        eight_wins = 0
        eight_percentage = 0
        for eight_match in eight_matches:
            if eight_match.won==True:
                eight_wins += 1
                # print("8", eight_match.won)
        try:
            eight_percentage = (eight_wins/eight_count)*100
        except ZeroDivisionError:
            eight_percentage = 0
        
        template = 'players/detail.html'
        context = {
            'player': player,
            'nine_matches': nine_matches,
            'eight_matches': eight_matches,
            'nine_percentage': nine_percentage,
            'eight_percentage': eight_percentage
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