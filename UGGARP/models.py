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
	#num of rounds in total
	num_rounds = 2
	#number of decision rounds
	decision_rounds=1
	#number of belief rounds
	belief_rounds=1
	belief_sequence = [4, 3, 7]


	#showup fee
	showup=8
	#benefit for belief -- to be updated...
	belief_payment = 1

	#defining the proposer earnigns for every round:
	proposer_earnings={}
	proposer_earnings['a'] = [35, 47, 59, 23, 46, 23, 69, 11.50, 57.50] 
	proposer_earnings['b'] = [33, 44, 55, 22, 44, 22, 66, 11, 55]
	proposer_earnings['c'] = [30, 40, 50, 20, 40, 20, 60, 10, 50]
	proposer_earnings['d'] = [27, 36, 45, 18, 36, 18, 54, 9, 45]
	proposer_earnings['e'] = [24, 32, 40, 16, 32, 16, 48, 8, 40]
	proposer_earnings['f'] = [21, 28, 35, 14, 28, 14, 42, 7, 35]
	proposer_earnings['g'] = [18, 24, 30, 12, 24, 12, 36, 6, 30]
	proposer_earnings['h'] = [15, 20, 25, 10, 20, 10, 30, 5, 25]
	proposer_earnings['i'] = [12, 16, 20, 8, 16, 8, 24, 4, 20]
	proposer_earnings['j'] = [9, 12, 15, 6, 12, 6, 18, 3, 15]
	proposer_earnings['k'] = [6, 8, 10, 4, 8, 4, 12, 2, 10]
	proposer_earnings['l'] = [3, 4, 5, 2, 4, 2, 6, 1, 5]
	proposer_earnings['m'] = [1, 1, 1, 1, 2, 1, 3, .50, 2.50]

	#defining responder earnings
	responder_earnings={}
	responder_earnings['a'] = [1, 1, 1, 2, 1, 3, 1, 2.50, .50]
	responder_earnings['b'] = [3, 4, 5, 4, 2, 6, 2, 5, 1]
	responder_earnings['c'] = [6, 8, 10, 8, 4, 12, 4, 10, 2]
	responder_earnings['d'] = [9, 12, 15, 12, 6, 18, 6, 15, 3]
	responder_earnings['e'] = [12, 16, 20, 16, 8, 24, 8, 20, 4]
	responder_earnings['f'] = [15, 20, 25, 20, 10, 30, 10, 25, 5]
	responder_earnings['g'] = [18, 24, 30, 24, 12, 36, 12, 30, 6]
	responder_earnings['h'] = [21, 28, 35, 28, 14, 42, 14, 35, 7]
	responder_earnings['i'] = [24, 32, 40, 32, 16, 48, 16, 40, 8]
	responder_earnings['j'] = [27, 36, 45, 36, 18, 54, 18, 45, 9]
	responder_earnings['k'] = [30, 40, 50, 40, 20, 60, 20, 50, 10]
	responder_earnings['l'] = [33, 44, 55, 44, 22, 66, 22, 55, 11]
	responder_earnings['m'] = [35, 47, 59, 46, 23, 69, 23, 57.50, 11.50]



class Subsession(BaseSubsession):
	#paying_round = models.IntegerField(initial=1)

	def before_session_starts(self):
		self.group_randomly()
		for g in self.get_groups():
			g.payment_round=random.randint(1,Constants.decision_rounds)
		

		

class Group(BaseGroup):
	proposer_earning = models.DecimalField(max_digits=5, decimal_places=1, default=0)
	responder_earning = models.DecimalField(max_digits=5, decimal_places=1, default=0)

	proposer_choice=models.CharField()
	responder_choice=models.CharField()

	payment_round=models.IntegerField()


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
			proposer.payment = decimal.Decimal(responder.responders_choice_a*proposer_option)
			responder.payment = decimal.Decimal(responder.responders_choice_a*responder_option)
			#define responder choice
			if responder.responders_choice_a == 0:
				self.responder_choice='Reject'
			else:
				self.responder_choice='Accept'
		elif menu_chosen=='b':
			proposer.payment = decimal.Decimal(responder.responders_choice_b*proposer_option)
			responder.payment = decimal.Decimal(responder.responders_choice_b*responder_option)

			if responder.responders_choice_b == 0:
				self.responder_choice='Reject'
			else:
				self.responder_choice='Accept'

		elif menu_chosen=='c':
			proposer.payment = decimal.Decimal(responder.responders_choice_c*proposer_option)
			responder.payment = decimal.Decimal(responder.responders_choice_c*responder_option)

			if responder.responders_choice_c == 0:
				self.responder_choice='Reject'
			else:
				self.responder_choice='Accept'
		elif menu_chosen=='d':
			proposer.payment = decimal.Decimal(responder.responders_choice_d*proposer_option)
			responder.payment = decimal.Decimal(responder.responders_choice_d*responder_option)
			
			if responder.responders_choice_d == 0:
				self.responder_choice='Reject'
			else:
				self.responder_choice='Accept'
		elif menu_chosen=='e':
			proposer.payment = decimal.Decimal(responder.responders_choice_e*proposer_option)
			responder.payment = decimal.Decimal(responder.responders_choice_e*responder_option)
			
			if responder.responders_choice_e == 0:
				self.responder_choice='Reject'
			else:
				self.responder_choice='Accept'
		elif menu_chosen=='f':
			proposer.payment = decimal.Decimal(responder.responders_choice_f*proposer_option)
			responder.payment = decimal.Decimal(responder.responders_choice_f*responder_option)
			
			if responder.responders_choice_f == 0:
				self.responder_choice='Reject'
			else:
				self.responder_choice='Accept'
		elif menu_chosen=='g':
			proposer.payment = decimal.Decimal(responder.responders_choice_g*proposer_option)
			responder.payment = decimal.Decimal(responder.responders_choice_g*responder_option)
			
			if responder.responders_choice_g == 0:
				self.responder_choice='Reject'
			else:
				self.responder_choice='Accept'

		elif menu_chosen=='h':
			proposer.payment = decimal.Decimal(responder.responders_choice_h*proposer_option)
			responder.payment = decimal.Decimal(responder.responders_choice_h*responder_option)
			
			if responder.responders_choice_h == 0:
				self.responder_choice='Reject'
			else:
				self.responder_choice='Accept'

		elif menu_chosen=='i':
			proposer.payment = decimal.Decimal(responder.responders_choice_i*proposer_option)
			responder.payment = decimal.Decimal(responder.responders_choice_i*responder_option)
			
			if responder.responders_choice_i == 0:
				self.responder_choice='Reject'
			else:
				self.responder_choice='Accept'

		elif menu_chosen=='j':
			proposer.payment = decimal.Decimal(responder.responders_choice_j*proposer_option)
			responder.payment = decimal.Decimal(responder.responders_choice_j*responder_option)
			
			if responder.responders_choice_j == 0:
				self.responder_choice='Reject'
			else:
				self.responder_choice='Accept'

		elif menu_chosen=='k':
			proposer.payment = decimal.Decimal(responder.responders_choice_k*proposer_option)
			responder.payment = decimal.Decimal(responder.responders_choice_k*responder_option)
			if responder.responders_choice_k == 0:
				self.responder_choice='Reject'
			else:
				self.responder_choice='Accept'

		elif menu_chosen=='l':
			proposer.payment = decimal.Decimal(responder.responders_choice_l*proposer_option)
			responder.payment = decimal.Decimal(responder.responders_choice_l*responder_option)
			
			if responder.responders_choice_l == 0:
				self.responder_choice='Reject'
			else:
				self.responder_choice='Accept'
		elif menu_chosen=='m':
			proposer.payment = decimal.Decimal(responder.responders_choice_m*proposer_option)
			responder.payment = decimal.Decimal(responder.responders_choice_m*responder_option)
			
			if responder.responders_choice_m == 0:
				self.responder_choice='Reject'
			else:
				self.responder_choice='Accept'
		self.responder_earning = responder.payment
		self.proposer_earning = proposer.payment


class Player(BasePlayer):
	#decision related variables and functions
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
	payment = models.DecimalField(max_digits=5, decimal_places=1, default=0)
	final_payment = models.DecimalField(max_digits=5, decimal_places=1, default=decimal.Decimal(Constants.showup))

	def get_partner(self):
		return self.get_others_in_group()[0]

	def get_final_payment(self):
		for p in self.in_all_rounds():
			if p.subsession.round_number==p.group.payment_round:
				self.final_payment=p.payment+8

	#belief related variables and functions
	belief_payments_round = models.IntegerField(initial=0)



	




