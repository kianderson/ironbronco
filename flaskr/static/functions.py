#!/usr/bin/env python
import requests
import json

# Participant class
class Participant:
    name = None
    email = None
    major = None
    team = None
    need = None

    def __init__(self, name, email, major, team, need):
        self.name = name
        self.email = email
        self.major = major
        self.team = team
        self.need = need

    def __repr__(self):
        return self.name

# Participant class
class Team:
    participant1 = None
    participant2 = None
    participant3 = None
    progress = {}

    def __init__(self, participant1, participant2, participant3):
        self.participant1 = participant1
        self.participant2 = participant2
        self.participant3 = participant3
        progress = {"Bike": 0, "Run": 0, "Swim": 0}

    def __repr__(self):
        return self.name

# progress functions
def logProgress(b, r, s):
    return

# TODO:
# progress board html
# pricing on profile Board
# self progress

# ------------------------------------------------------------------------------
# GET
