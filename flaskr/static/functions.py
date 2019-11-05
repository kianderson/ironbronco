#!/usr/bin/env python
import requests
import json

def hello():
    print('hello world')

# Participant class
class Participant:
    name = None
    email = None
    major = None
    team = None
    need = None

    def __init__(self, name, email, major, team, need): # add password
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
    stats = {}
    percent = None

    def __init__(self, participant1, participant2, participant3):
        self.participant1 = participant1
        self.participant2 = participant2
        self.participant3 = participant3
        self.stats = {"Bike": 0, "Run": 0, "Swim": 0}
        self.percent = 0

    def __repr__(self):
        return self.name

# ------------------------------------------------------------------------------
# create team
'''
# adds class team to db
def createTeam(teamName, email1, email2, email3):
    # checks if each user is in DATABASE
    if (email1 != None):
        # participant 1
        participant1 = getParticipant(email)

        # participant 2
        if (email2 == None):
            participant2 = None
        else:
            participant2 = getParticipant(email)

        # participant 3
        if (email3 == None):
            participant3 = None
        else:
            participant3 = getParticipant(email)

        team = Team(participant1, participant2, participant3)
        # need to check for case if user does not exist or is invalid
        return
    else:
        invalid, not a team
        return

def getParticipant(email):
    if (userExists(email) == True):
        return an object of class participant
    else:
        return not valid user

# ------------------------------------------------------------------------------
# login

def login(email, password):
    # checks passwords and users to see if valid
    if (userExists(email) == True):
        if (password matches to email):
            login successful
        else:
            incorrect login
    else:
        incorrect login

# ------------------------------------------------------------------------------
# profile board

# sort table by people who have a team vs. dont TODO: LATER

# loads all participants, emails, if they are on a team, what they are looking for, maybe gray out people who already have a team
def getTeams():
    r = requests.get(STUFF GOES HERE)
    teams = r.json()

# ------------------------------------------------------------------------------
# progress

# log
def logWorkout(team, b, r, s):
    # convert laps to miles
    s = (s/86.5)*2.4
    # add brs and user to DATABASE

    updateProgress(team)
    return

# recalculate progress function
def updateProgress(team):
    # grab team's logs from db and store in b, r, s
    team.stats["Bike"] = b
    team.progress = calculateProgress(team)
    return

def calculateProgress(team):
    bikePercent = (team.stats["Bike"]/112)*100
    runPercent = (team.stats["Run"]/26.2)*100
    swimPercent = (team.stats["Swim"]/2.4)*100
    percent = (bikePercent + runPercent + swimPercent)/3
    return percent

# ------------------------------------------------------------------------------
# register

def register(name, email, major, team, need):
    if (userExists(email) == False):
        # create instance of class Participant
        participant = Participant(name, email, major, team, need)
    else:
        # display error message
    return

# function that checks if user already exists in db
def userExists(email):
    if email in db:
        return True
    else:
        return False

# ------------------------------------------------------------------------------
# TODO:
# progress board html
# pricing on profile Board
# self progress
# add description of what race is
# register needs a password

# ------------------------------------------------------------------------------
# GET
'''
