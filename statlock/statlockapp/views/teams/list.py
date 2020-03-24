import sqlite3
from ..connection import Connection
from django.shortcuts import render, reverse, redirect
from statlockapp.models import Team, Player
from django.contrib.auth.decorators import login_required

@login_required
def team_list(request):
    if request.method == 'GET':
        team = Team.objects.get(id=request.user.captain.team_id)
        test_team = team
        team_members = Player.objects.filter(team__id=request.user.captain.team_id)


        template = 'teams/team_list.html'
        context = {
            'all_players': team_members.values(),
            'team': team,
            'test_team': test_team
        }

        return render(request, 'teams/team_list.html', context)



