from django.urls import include, path
from .views import *

app_name = "statlockapp"

urlpatterns = [
    path('', home, name='home'),
    path('team/', team_list, name='team'),
    path('lineup/', lineup_list, name='lineup'),
    path('lineups/<int:team_id>/', opp_lineup, name='opplineup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('player/form', player_form, name='player_form'),
    path('players/<int:player_id>/form/', player_edit_form, name='player_edit_form'),
    path('players/<int:player_id>/', player_details, name='player'),
    path('match/form', match_form, name='match_form'),
    path('matches/<int:match_id>/form/', match_edit_form, name='match_edit_form'),
    path('matches/<int:match_id>/', match_details, name='match'),
    path('team/form', team_form, name='team_form'),
]
