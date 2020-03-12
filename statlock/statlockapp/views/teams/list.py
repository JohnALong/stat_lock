import sqlite3
from ..connection import Connection
from django.shortcuts import render, reverse, redirect
from statlockapp.models import Team
from django.contrib.auth.decorators import login_required

# @login_required
def team_list(request):
    if request.method == 'GET':

        all_teams = Team.objects.all()


        template = 'teams/team_list.html'
        context = {
            'all_teams': all_teams
        }

        return render(request, template, context)
        


