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
Questionnare for Collective Experimentation Project with C. Martinelli"""


class Constants(BaseConstants):
	name_in_url = 'questionnaire'
	players_per_group = None
	num_rounds = 1


class Subsession(BaseSubsession):
	pass


class Group(BaseGroup):
	pass


class Player(BasePlayer):
	Gender = models.CharField(choices=[('M','Male'), ('F','Female')],default='M')
	Major = models.CharField()
	Age = models.IntegerField(min=18, max=99)
	NumOfSiblings = models.IntegerField(min=0,max=100)
	Ethnicity = models.CharField(choices=[('W','White'),('B','Black'), ('H','Hispanic'), ('A','Asian'), ('O','Other')])
	Experienced = models.CharField(choices=[('Y','Yes'),('N','No')])
	YearInCollege = models.CharField(choices=[('F','Freshman'), ('So','Sophomore'), ('J','Junior'),('Se','Senior'), ('GS','Graduate Student')])
	GPA = models.DecimalField(max_digits=3, decimal_places=2, default=0)

