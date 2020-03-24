import sqlite3
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from statlockapp.models import Captain, Team
from ..connection import Connection

@csrf_exempt
def register(request):

    if request.method == 'GET':
        teams = Team.objects.all()

        template = 'registration/register.html'
        context = {
            'all_teams': teams
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        new_user = User.objects.create_user(
            username=form_data['username'],
            first_name=form_data['first_name'],
            last_name=form_data['last_name'],
            email=form_data['email'],
            password=form_data['password'])
        

        new_captain = Captain.objects.create(
            user=new_user,
            team_id=form_data['team']
        )
        new_user = authenticate(username=form_data['username'], password=form_data['password'],
                                    )
        login(request, new_user)

    return redirect(reverse('statlockapp:home'))

    