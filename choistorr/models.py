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
    players_per_group = 2
    num_rounds = 100

    upper_bar = 500
    lower_bar = 500

    costs_of_y = 30
    costs_of_switch = 20

    low_profit_y = 10
    high_profit_y = 15




class Subsession(BaseSubsession):
    random_number=models.IntegerField(initial=7)

    next_round = models.IntegerField(min=1,max=Constants.num_rounds)

    def compute_next_round(self):
    	self.next_round = self.round_number+1

    def determine_round_end(self):
        self.random_number = random.randint(1,6)


class Group(BaseGroup):
    num_of_x_choosers = models.IntegerField(min=0,max=Constants.players_per_group,initial=0)
    num_of_y_choosers = models.IntegerField(min=0,max=Constants.players_per_group,initial=0)

    def set_payoffs(self):
    	for p in self.get_players():
    		p.set_payoffs()

    def find_y_choosers(self):
    	for p in self.get_players():
    		if p.action == 'Y':
    			self.num_of_y_choosers=self.num_of_y_choosers+1


class Player(BasePlayer):
#endowment of player

	endowment = models.IntegerField(min=0,initial=500) #randint(Constants.lower_bar,Constants.upper_bar)
	previous_endowment = models.IntegerField(min=0)
	earning = models.IntegerField(min=0,initial=0)
#taking action in every stage

	action = models.CharField(
		choices=[('X'), ('Y')],
		widget=widgets.RadioSelect()
		)
#the forecast var for the forecast stage
	forecast = models.IntegerField(min=0,max=Constants.players_per_group)
#start methods definitions:

	def set_payoffs(self):
		
		if self.subsession.round_number>1:
			p = self.in_round(self.subsession.round_number-1)
			self.endowment=p.endowment
			
		if self.action=='Y':
			if self.group.num_of_y_choosers<=Constants.players_per_group/2:
				self.earning=(self.group.num_of_y_choosers-1)*Constants.low_profit_y - Constants.costs_of_y

			if self.group.num_of_y_choosers>Constants.players_per_group/2:
				self.earning=(self.group.num_of_y_choosers-1)*Constants.high_profit_y - Constants.costs_of_y

		if self.action=='X' and self.subsession.round_number>1:
			if p.action =='Y':
				self.earning= - Constants.costs_of_switch

		self.previous_endowment=self.endowment
		self.endowment=self.endowment+self.earning
