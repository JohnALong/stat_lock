import sqlite3
from ..connection import Connection
from django.shortcuts import render, reverse, redirect
from statlockapp.models import Team, Player
from django.contrib.auth.decorators import login_required

# @login_required
def team_list(request):
    if request.method == 'GET':

        team_members = Player.objects.all()



        # template = 'teams/team_list.html'
        context = {
            'all_players': team_members
        }

        return render(request, 'teams/team_list.html', context)

