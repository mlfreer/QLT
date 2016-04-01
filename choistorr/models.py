# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

author = 'Your name here'

doc = """
Infinitely repeating PGG, with prediction stage. Default setting = Treatment 1 (homogenuous values).
Changing upper_bar and lower_bar will make the setting into heterogeneous endowments
"""


class Constants(BaseConstants):
    name_in_url = 'choistorr'
    players_per_group = 5
    num_rounds = 1

    upper_bar = 500
    lower_bar = 500


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
#endowment of player
	endowment = models.IntegerField(min=0) #randint(Constants.lower_bar,Constants.upper_bar)

#taking action in every stage

	action = models.CharField(
		choices=[('X'), ('Y')],
		widget=widgets.RadioSelect()
		)
#the forecast var for the forecast stage	
	forecast = models.IntegerField(min=0,max=Constants.players_per_group)
