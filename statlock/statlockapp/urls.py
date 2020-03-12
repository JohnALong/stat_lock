from django.urls import include, path
from .views import *

app_name = "statlockapp"

urlpatterns = [
    path('', home, name='home'),
    path('team/', team_list, name='team'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register')
]
