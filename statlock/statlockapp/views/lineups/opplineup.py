import sqlite3
from django.urls import reverse
from django.db.models import Count, F
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from statlockapp.models import Player, Match, Team
from itertools import combinations
from ..connection import Connection

@login_required
def opp_lineup(request, team_id):

    if request.method == 'GET':
        user_team = Team.objects.get(id=request.user.captain.team_id)
        opp_team = Team.objects.get(id=team_id)
        # print("opp team", opp_team.name)
        # print("user team", user_team.name)
        opp_players = Player.objects.filter(team_id=team_id)
        opp_eight_ratings = []
        opp_nine_ratings = []
        for opp_player in opp_players:
            opp_eight_ratings.append(opp_player.eight_rating)
            opp_nine_ratings.append(opp_player.nine_rating)

        opp_nine_combos = list(combinations(opp_nine_ratings, 5))
        opp_nine_listed_combos = list(map(list, opp_nine_combos))
        opp_nine_no_duplicates = []
        opp_nine_under_23s = []
        for opp_nine_listed_combo in opp_nine_listed_combos:
            opp_nine_listed_combo.sort()
            if opp_nine_listed_combo not in opp_nine_no_duplicates:
                opp_nine_no_duplicates.append(opp_nine_listed_combo)

        # print("no duplicates", nine_no_duplicates)
        for opp_nine_no_duplicate in opp_nine_no_duplicates:
            if sum(opp_nine_no_duplicate) <= 23 and opp_nine_no_duplicate not in opp_nine_under_23s:
                opp_nine_under_23s.append(opp_nine_no_duplicate)
        # print("23 check", opp_nine_under_23s)

        # start of opp 8 ball data
        opp_eight_combos = list(combinations(opp_eight_ratings, 5))
        opp_eight_listed_combos = list(map(list, opp_eight_combos))
        opp_eight_no_duplicates = []
        opp_eight_under_23s = []
        for opp_eight_listed_combo in opp_eight_listed_combos:
            opp_eight_listed_combo.sort()
            if opp_eight_listed_combo not in opp_eight_no_duplicates:
                opp_eight_no_duplicates.append(opp_eight_listed_combo)

        # print("no duplicates", nine_no_duplicates)
        for opp_eight_no_duplicate in opp_eight_no_duplicates:
            if sum(opp_eight_no_duplicate) <= 23 and opp_eight_no_duplicate not in opp_eight_under_23s:
                opp_eight_under_23s.append(opp_eight_no_duplicate)
        # print("23 check 8's", opp_eight_under_23s)

        user_team_members = Player.objects.filter(team__id=request.user.captain.team_id)
        user_eight_ratings = []
        user_nine_ratings = []
        for user_member in user_team_members:
            user_eight_ratings.append(user_member.eight_rating)
            user_nine_ratings.append(user_member.nine_rating)

        # attempt to get all combinations of skill levels max 5 of 8 for 9 ball
        user_nine_combos = list(combinations(user_nine_ratings, 5))
        # combos is a list of tuples
        user_nine_listed_combos = list(map(list, user_nine_combos))
        user_nine_no_duplicates = []
        user_nine_under_23s = []
        # print("listed_combos", listed_combos)
        for user_nine_listed_combo in user_nine_listed_combos:
            user_nine_listed_combo.sort()
            # print("listed_combo", nine_listed_combo)
            if user_nine_listed_combo not in user_nine_no_duplicates:
                user_nine_no_duplicates.append(user_nine_listed_combo)

        # print("no duplicates", nine_no_duplicates)
        for user_nine_no_duplicate in user_nine_no_duplicates:
            if sum(user_nine_no_duplicate) <= 23 and user_nine_no_duplicate not in user_nine_under_23s:
                user_nine_under_23s.append(user_nine_no_duplicate)
                # print("23 check", nine_under_23s)

        # attempt to get all combinations of skill levels max 5 of 8 for 8 ball
        user_combos = list(combinations(user_eight_ratings, 5))
        # combos is a list of tuples
        user_listed_combos = list(map(list, user_combos))
        user_no_duplicates = []
        user_eight_under_23s = []
        # print("listed_combos", listed_combos)
        for user_listed_combo in user_listed_combos:
            user_listed_combo.sort()
            # print("listed_combo", listed_combo)
            if user_listed_combo not in user_no_duplicates:
                user_no_duplicates.append(user_listed_combo)

        # print("no duplicates", no_duplicates)
        for user_no_duplicate in user_no_duplicates:
            if sum(user_no_duplicate) <= 23 and user_no_duplicate not in user_eight_under_23s:
                user_eight_under_23s.append(user_no_duplicate)
                # print("23 check", eight_under_23s)


        
        template = 'lineups/opplineup.html'
        context = {
            'opp_players': opp_players,
            'user_all_players': user_team_members.values(),
            'user_team': user_team,
            'opp_team': opp_team,
            'user_eight_under_23s': user_eight_under_23s,
            'user_nine_under_23s': user_nine_under_23s,
            'opp_nine_under_23s': opp_nine_under_23s,
            'opp_eight_under_23s': opp_eight_under_23s
        }

        return render(request, template, context)