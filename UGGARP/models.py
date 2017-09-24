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
Ultimatum Game for Castillo, Cross and Freer paper on Nonparametric Utility Theory. 
Including the point elicitation of the beliefs using the Houssain and Okui (2013).
"""


class Constants(BaseConstants):
	name_in_url = 'uggarp'
	players_per_group = 2
	num_rounds = 1

	#showup fee
	showup=8

	#defining the proposer earnigns for every round:
	proposer_earnings={}
	proposer_earnings['a']=[35, 47] 
	proposer_earnings['b'] = [33, 44]
	proposer_earnings['c'] = [30, 40]
	proposer_earnings['d'] = [27, 36]
	proposer_earnings['e'] = [24, 32]
	proposer_earnings['f'] = [21, 28]
	proposer_earnings['g'] = [18, 24]
	proposer_earnings['h'] = [15, 20]
	proposer_earnings['i'] = [12, 16]
	proposer_earnings['j'] = [9, 12]
	proposer_earnings['k'] = [6, 8]
	proposer_earnings['l'] = [3, 4]
	proposer_earnings['m'] = [1, 1]

	#defining responder earnings
	responder_earnings={}
	responder_earnings['a'] = [1, 1]
	responder_earnings['b'] = [3, 4]
	responder_earnings['c'] = [6, 8]
	responder_earnings['d'] = [9, 12]
	responder_earnings['e'] = [12, 16]
	responder_earnings['f'] = [15, 20]
	responder_earnings['g'] = [18, 24]
	responder_earnings['h'] = [21, 28]
	responder_earnings['i'] = [24, 32]
	responder_earnings['j'] = [27, 36]
	responder_earnings['k'] = [30, 40]
	responder_earnings['l'] = [33, 44]
	responder_earnings['m'] = [35, 47]



class Subsession(BaseSubsession):
	paying_round = models.IntegerField(initial=1)

	def before_session_starts(self):
		self.group_randomly()
		for g in self.get_groups():
			g.paying_round=random.randint(1,Constants.num_rounds)

		

class Group(BaseGroup):
	result=models.IntegerField(initial=0)

	proposer_choice=models.CharField()
	responder_choice=models.CharField()

	pyment_round=models.IntegerField()


	def get_player_payment(self):
		#define who is proposer
		r = random.uniform(0,1)
		if r<=.5:
			proposer = self.get_players()[0]
			responder = self.get_players()[1]
		else:
			proposer = self.get_players()[1]
			responder = self.get_players()[0]

		#get roles down to players
		proposer.role = 'Proposer'
		responder.role= 'Responder'
		#get actions:
		self.proposer_choice = proposer.proposers_choice


		#which menu we are considering and which option has been chosen
		
		menu_number = self.subsession.round_number-1
		menu_chosen = proposer.proposers_choice
		proposer_option = Constants.proposer_earnings[proposer.proposers_choice][menu_number]
		responder_option = Constants.responder_earnings[proposer.proposers_choice][menu_number]
		#switching among menues
		if menu_chosen=='a':
			proposer.payment = responder.responders_choice_a*proposer_option
			responder.payment = responder.responders_choice_a*responder_option
			#define responder choice
			if responder.responders_choice_a == 0:
				responder_choice='Reject'
			else:
				responder_choice='Accept'
		elif manu_chosen=='b':
			roposer.payment = responder.responders_choice_b*proposer_option
			responder.payment = responder.responders_choice_b*responder_option

			if responder.responders_choice_b == 0:
				responder_choice='Reject'
			else:
				responder_choice='Accept'

		elif manu_chosen=='c':
			roposer.payment = responder.responders_choice_c*proposer_option
			responder.payment = responder.responders_choice_c*responder_option

			if responder.responders_choice_c == 0:
				responder_choice='Reject'
			else:
				responder_choice='Accept'
		elif manu_chosen=='d':
			roposer.payment = responder.responders_choice_d*proposer_option
			responder.payment = responder.responders_choice_d*responder_option
			
			if responder.responders_choice_d == 0:
				responder_choice='Reject'
			else:
				responder_choice='Accept'
		elif manu_chosen=='e':
			roposer.payment = responder.responders_choice_e*proposer_option
			responder.payment = responder.responders_choice_e*responder_option
			
			if responder.responders_choice_e == 0:
				responder_choice='Reject'
			else:
				responder_choice='Accept'
		elif manu_chosen=='f':
			roposer.payment = responder.responders_choice_f*proposer_option
			responder.payment = responder.responders_choice_f*responder_option
			
			if responder.responders_choice_f == 0:
				responder_choice='Reject'
			else:
				responder_choice='Accept'
		elif manu_chosen=='g':
			roposer.payment = responder.responders_choice_g*proposer_option
			responder.payment = responder.responders_choice_g*responder_option
			
			if responder.responders_choice_g == 0:
				responder_choice='Reject'
			else:
				responder_choice='Accept'

		elif manu_chosen=='h':
			roposer.payment = responder.responders_choice_h*proposer_option
			responder.payment = responder.responders_choice_h*responder_option
			
			if responder.responders_choice_h == 0:
				responder_choice='Reject'
			else:
				responder_choice='Accept'

		elif manu_chosen=='i':
			roposer.payment = responder.responders_choice_i*proposer_option
			responder.payment = responder.responders_choice_i*responder_option
			
			if responder.responders_choice_i == 0:
				responder_choice='Reject'
			else:
				responder_choice='Accept'

		elif manu_chosen=='j':
			roposer.payment = responder.responders_choice_j*proposer_option
			responder.payment = responder.responders_choice_j*responder_option
			
			if responder.responders_choice_j == 0:
				responder_choice='Reject'
			else:
				responder_choice='Accept'

		elif manu_chosen=='k':
			roposer.payment = responder.responders_choice_k*proposer_option
			responder.payment = responder.responders_choice_k*responder_option
			if responder.responders_choice_k == 0:
				responder_choice='Reject'
			else:
				responder_choice='Accept'

		elif manu_chosen=='l':
			roposer.payment = responder.responders_choice_l*proposer_option
			responder.payment = responder.responders_choice_l*responder_option
			
			if responder.responders_choice_l == 0:
				responder_choice='Reject'
			else:
				responder_choice='Accept'
		elif manu_chosen=='m':
			roposer.payment = responder.responders_choice_m*proposer_option
			responder.payment = responder.responders_choice_m*responder_option
			
			if responder.responders_choice_m == 0:
				responder_choice='Reject'
			else:
				responder_choice='Accept'


class Player(BasePlayer):
	proposers_choice=models.CharField(choices=['a','b','c','d','e','f','g','h','i','j','k','l','m'])
	responders_choice_a = models.IntegerField(initial=0)
	responders_choice_b = models.IntegerField(initial=0)
	responders_choice_c = models.IntegerField(initial=0)
	responders_choice_d = models.IntegerField(initial=0)
	responders_choice_e = models.IntegerField(initial=0)
	responders_choice_f = models.IntegerField(initial=0)
	responders_choice_g = models.IntegerField(initial=0)
	responders_choice_h = models.IntegerField(initial=0)
	responders_choice_i = models.IntegerField(initial=0)
	responders_choice_j = models.IntegerField(initial=0)
	responders_choice_k = models.IntegerField(initial=0)
	responders_choice_l = models.IntegerField(initial=0)
	responders_choice_m = models.IntegerField(initial=0)

	role = models.CharField(choices=['Proposer','Responder'])
	payment = models.IntegerField(initial=0)
	final_payment = models.IntegerField(initial=Constants.showup)

	def get_partner(self):
		return self.get_others_in_group()[0]

	def get_final_payment(self):
		for p in player.in_all_rounds():
			if p.subsession.round_number==p.group.payment_round:
				self.final_payment=p.payment+8


	




