from django.urls import path
from .views import *

app_name = "statlockapp"

urlpatterns = [
    path('', home, name='home'),
    path('teams/', team_list, name='teams'),
]
