# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random
import decimal

import otree.models
from otree.db import models

from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'qlt'
    players_per_group = None
    num_rounds = 30
    endowment = c(100)


class Subsession(BaseSubsession):

	paying_round = models.IntegerField()

	def before_session_starts(self):
		for p in self.get_players():
			p.set_prices()
			if self.round_number == Constants.num_rounds:
				self.paying_round = random.randint(1, Constants.num_rounds)
				self.session.vars['paying_round'] = self.paying_round
    #pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
#defining quantity vars
	CashQuantity = models.IntegerField(initial=0)
	MasonMoneyQuantity = models.IntegerField(initial=0)
	BarnesNobleQuantity = models.IntegerField(initial=0)
	FandangoQuantity = models.IntegerField(initial=0)
	GapQuantity = models.IntegerField(initial=0)

#defining price vars
	CashPrice = models.DecimalField(..., max_digits=5, decimal_places=1, default=0)
	MasonMoneyPrice = models.DecimalField(..., max_digits=5, decimal_places=1, default=0)
	BarnesNoblePrice = models.DecimalField(..., max_digits=5, decimal_places=1, default=0)
	FandangoPrice = models.DecimalField(..., max_digits=5, decimal_places=1, default=0)
	GapPrice = models.DecimalField(..., max_digits=5, decimal_places=1, default=0)

#defining spending vars
	CashSpending = models.DecimalField(..., max_digits=5, decimal_places=1, default=0)
	MasonMoneySpending = models.DecimalField(..., max_digits=5, decimal_places=1, default=0)
	BarnesNobleSpending = models.DecimalField(..., max_digits=5, decimal_places=1, default=0)
	FandangoSpending = models.DecimalField(..., max_digits=5, decimal_places=1, default=0)
	GapSpending = models.DecimalField(..., max_digits=5, decimal_places=1, default=0)

	Expenditure = models.DecimalField(..., max_digits=5, decimal_places=1, default=0)

	def compute_spendings(self):
		self.CashSpending = self.CashPrice*decimal.Decimal(self.CashQuantity)
		self.MasonMoneySpending = self.MasonMoneyPrice*decimal.Decimal(self.MasonMoneyQuantity)
		self.BarnesNobleSpending = self.BarnesNoblePrice*decimal.Decimal(self.BarnesNobleQuantity)
		self.FandangoSpending = self.FandangoPrice*decimal.Decimal(self.FandangoQuantity)
		self.GapSpending = self.GapPrice*decimal.Decimal(self.GapQuantity)

		self.Expenditure = self.CashSpending+self.MasonMoneySpending+self.BarnesNobleSpending+self.FandangoSpending+self.GapSpending


	def set_prices(self):
		self.CashPrice = random.randint(5,30)/2
		self.MasonMoneyPrice = 17.5 - self.CashPrice

		self.FandangoPrice = random.randrange(5,14)/2

		self.BarnesNoblePrice = random.randrange(5,20)/2
		self.GapPrice = 12.5 - self.BarnesNoblePrice

#questionnaires

	Q1 = models.CharField(
    	choices=['Yes', 'No'],
    	widget=widgets.RadioSelect()
    )

	Q2 = models.CharField(
    	choices=['Yes', 'No'],
    	widget=widgets.RadioSelect()
    )

	Q3 = models.CharField(
    	choices=['Yes', 'No'],
    	widget=widgets.RadioSelect()
    )

	Q4 = models.CharField(
    	choices=['Yes', 'No'],
    	widget=widgets.RadioSelect()
    )

	Q5 = models.CharField(
    	choices=['Yes', 'No'],
    	widget=widgets.RadioSelect()
    )

	Gender = models.CharField(choices=[('M','Male'), ('F','Female')],default='M')
	Age = models.IntegerField(min=18, max=99)
	ShareFood = models.CurrencyField(min=0, max=100)
	ShareBooks = models.CurrencyField(min=0, max=100)
	ShareCloths = models.CurrencyField(min=0, max=100)
	ShareMovies = models.CurrencyField(min=0, max=100)

	AllArrived = models.IntegerField(initial=0)

	def all_arrive(self):
		AllArrived=1

