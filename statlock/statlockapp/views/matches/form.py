import sqlite3
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from statlockapp.models import Player, Match, MatchType
from ..connection import Connection

@login_required
def match_form(request):

    if request.method == 'GET':
        all_players = Player.objects.all()
        all_matchtypes = MatchType.objects.all()

        template = 'matches/form.html'
        context = {
            'all_players': all_players,
            'all_matchtypes': all_matchtypes
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        match_won = form_data.get("won", False)

        new_match = Match.objects.create(
            match_type_id=form_data['matchtype'],
            player_id=form_data['player'],
            won = match_won)

    return redirect(reverse('statlockapp:team'))

@login_required
def match_edit_form(request, match_id):

    if request.method == 'GET':
        match = Match.objects.get(id=match_id)

        template = 'matches/form.html'
        context = {
            'match': match
        }

        return render(request, template, context)