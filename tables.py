import json
from peewee import *
import datetime

with open('config/config.json') as f:
    config = json.load(f)

db = SqliteDatabase(config["database"]["path"])


class User(Model):
    user_id = IntegerField(primary_key=True)     # telegram user ID
    group = IntegerField()                  # each user can belong to only one group
    dci = IntegerField(null=True)           # dci wotc gamer number
    name = CharField()
    arena = CharField(null=True)            # mtg arena player username
    win = IntegerField(default=0)           # total wins
    lose = IntegerField(default=0)          # total match lost
    lgs_points = IntegerField(default=0)    # points assigned in LGS leagues
    dci_points = IntegerField(null=True)    # dci planeswalker points
    status = IntegerField(default=0)        # bot navigation based on FSM machine

    class Meta:
        database = db


class Event(Model):
    event_id = IntegerField()
    name = CharField()          # event title
    type = CharField(null=True)          # fnm, draft, constructed, ...
    date = DateTimeField(default=datetime.date.today() + datetime.timedelta(days=1))      # planned event day
    expired = BooleanField(default=False)
    prize = CharField(null=True)
    infos = CharField(null=True)         # further infos about the event
    subs = IntegerField(default=0)       # total subscribers to this event
    winner = IntegerField(null=True)     # player ID who went first

    class Meta:
        database = db


class Round(Model):
    event_id = IntegerField()   # an event id
    round = IntegerField(default=1)      # round number
    player1 = IntegerField(null=True)    # first player ID
    player2 = IntegerField(null=True)    # second player ID
    winner = IntegerField(null=True)     # winner player ID
    home = IntegerField(null=True)       # player 1 points on 3 rounds
    visitor = IntegerField(null=True)    # player 2 points on 3 rounds (ex: 2-1)

    class Meta:
        database = db