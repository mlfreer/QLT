# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random
import decimal

import random

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

author = 'Mikhail Freer'

doc = """
Project for Collective Experimentation: An Experiment paper with Cesar Martinelli and Siyu Wang.
"""


class Constants(BaseConstants):
    name_in_url = 'CollectiveExperimentation'
    players_per_group = 3
    num_rounds = 1
    High = 500 #payoff for High Type| Risky Alternative is Chosen
    Low = 100 # payoff for Low Type|Risky Alternative is Chosen
    Safe = 300 #payoff from the Safe Alernative
    p = .5 #probability of being a High Type
    q = .5 #probability of type disclosure



class Subsession(BaseSubsession):
    paying_round = models.IntegerField()
    #functions at the subsession level
    def before_session_starts(self):
        self.group_randomly()



class Group(BaseGroup):
    RiskyChosen = IntegerField(initial = 0) #is risky alternative chosen
    Votes2Start = IntegerField(initial = 0) #the amount of people voted to start (Stage 1)
    Votes2Continue = IntegerField(initial = 0) #the amount of people voted to continue experimenting (Stage 2)
    Votes2Implement = IntegerField(initial = 0) #the amount of people voted to implement RA (Stage 3)



class Player(BasePlayer):
    Type = IntegerField() #=type of player: 1 = High, 0 = Low
    Signal1 = IntegerField(initial=0) #= signal at the stage 1: 1=High, 0=Uncertain
    Signal2 = IntegerField(initial=0) #= signal at the stage 2: 1=High, 0=Uncertain

    #next comes the verbalized versions of signals, for the views
    VerbalSignal1 = CharField(choices = ['Uncertain', 'High'])
    VerbalSignal2 = CharField(choices=['Uncertain','High'])

    #decision variables: 3 stages of voting
    VoteStage1 = IntegerField(initial=0)
    VoteStage2 = IntegerField(initial=0)
    VoteStage3 = IntegerField(initial=0)
    #verbalized decisions:
    VerbalVoteStage1 = CharField(
    	choices=['Yes','No']
    	widgets=widgets.RadioSelect()
    	)
    VerbalVoteStage2 = CharField(
    	choices=['Yes','No']
    	widgets=widgets.RadioSelect()
    	)
    VerbalVoteStage3 = CharField(
    	choices=['Yes','No']
    	widgets=widgets.RadioSelect()
    	)

    #functions for the player
    def get_vote_stage1(slef):
    	if self.VerbalVoteStage1 == 'Yes':
    		self.VoteStage1=1
    		


