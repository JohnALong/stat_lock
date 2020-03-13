import sqlite3
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from statlockapp.models import Player, Team, Captain
from ..connection import Connection

def player_form(request):

    if request.method == 'GET':
        team = Team.objects.get(id=request.user.captain.team_id)

        template = 'players/form.html'
        context = {
            'team': team
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        new_player = Player.objects.create(
            name=form_data['name'],
            eight_rating=form_data['eight_rating'],
            nine_rating=form_data['nine_rating'],
            team_id=request.user.captain.team_id)

        new_player.save()

    return redirect(reverse('statlockapp:team'))