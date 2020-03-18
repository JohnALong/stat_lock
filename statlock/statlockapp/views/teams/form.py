import sqlite3
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from statlockapp.models import Team, Captain
from ..connection import Connection

@login_required
def team_form(request):

    if request.method == 'GET':
        captain = Captain.objects.get(id=request.user.captain.id)

        template = 'teams/form.html'
        context = {
            'captain': captain
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        new_team = Team.objects.create(
            name=form_data['name'])

        captain_to_update = Captain.objects.get(pk=request.user.captain.id)

        captain_to_update.team_id = new_team.id
        captain_to_update.user_id = request.user.id

        captain_to_update.save()

    return redirect(reverse('statlockapp:team'))