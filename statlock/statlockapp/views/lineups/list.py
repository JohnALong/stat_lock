import sqlite3
from ..connection import Connection
from django.shortcuts import render, reverse, redirect
from statlockapp.models import Team, Player
from django.contrib.auth.decorators import login_required
from itertools import combinations

@login_required
def lineup_list(request):
    if request.method == 'GET':
        team = Team.objects.get(id=request.user.captain.team_id)
        team_members = Player.objects.filter(team__id=request.user.captain.team_id)
        opp_teams = Team.objects.all().exclude(id=team.id)
        # opp_teams = Team.objects.filter(team_id=teams.id).exclude(id=team.id)
        # print("opp_teams", opp_teams)
        eight_ratings = []
        nine_ratings = []
        for member in team_members:
            eight_ratings.append(member.eight_rating)
            nine_ratings.append(member.nine_rating)
        # print("eight_ratings", eight_ratings)
        # print("nine_ratings", nine_ratings)

        # attempt to get all combinations of skill levels max 5 of 8 for 9 ball
        nine_combos = list(combinations(nine_ratings, 5))
        # combos is a list of tuples
        nine_listed_combos = list(map(list, nine_combos))
        nine_no_duplicates = []
        nine_under_23s = []
        # print("listed_combos", listed_combos)
        for nine_listed_combo in nine_listed_combos:
            nine_listed_combo.sort(reverse=True)
            # print("listed_combo", nine_listed_combo)
            if nine_listed_combo not in nine_no_duplicates:
                nine_no_duplicates.append(nine_listed_combo)

        # print("no duplicates", nine_no_duplicates)
        for nine_no_duplicate in nine_no_duplicates:
            if sum(nine_no_duplicate) <= 23 and nine_no_duplicate not in nine_under_23s:
                nine_under_23s.append(nine_no_duplicate)
                # print("23 check", nine_under_23s)

        # attempt to get all combinations of skill levels max 5 of 8 for 8 ball
        combos = list(combinations(eight_ratings, 5))
        # combos is a list of tuples
        listed_combos = list(map(list, combos))
        no_duplicates = []
        eight_under_23s = []
        # print("listed_combos", listed_combos)
        for listed_combo in listed_combos:
            listed_combo.sort(reverse=True)
            # print("listed_combo", listed_combo)
            if listed_combo not in no_duplicates:
                no_duplicates.append(listed_combo)

        # print("no duplicates", no_duplicates)
        for no_duplicate in no_duplicates:
            if sum(no_duplicate) <= 23 and no_duplicate not in eight_under_23s:
                eight_under_23s.append(no_duplicate)
                # print("23 check", eight_under_23s)

        template = 'lineups/lineup_list.html'
        context = {
            'all_players': team_members.values(),
            'team': team,
            'opp_teams': opp_teams,
            'eight_under_23s': eight_under_23s,
            'nine_under_23s': nine_under_23s
        }

        return render(request, 'lineups/lineup_list.html', context)