from django.contrib import admin
from django.db import models

from bgame.models import Game, Team, Period

admin.site.register(Game)
admin.site.register(Team)
admin.site.register(Period)
