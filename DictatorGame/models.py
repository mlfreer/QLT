from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)

from otree.db import models
from django.db import models

import random
import decimal
import random

author = 'Mikhail Freer'

doc = """
Dictator Game
"""


class Constants(BaseConstants):
	name_in_url = 'DictatorGame'
	players_per_group = 2
	num_rounds = 1
	endowment = 40


class Subsession(BaseSubsession):
	pass


class Group(BaseGroup):
	def compute_payments(self):
		for p in self.get_players():
			p.get_hold()

		for p in self.get_players():
			p.get_payment()


class Player(BasePlayer):
	Pass = models.IntegerField(default =0)
	Hold = models.IntegerField(default = 40)

	Payment = models.IntegerField(default = 40)

	def get_hold(self):
		self.Hold = 40 - self.Pass

	def get_partner(self):
		return self.get_others_in_group()[0]
	
	def get_payment(self):
		p=self.get_partner()
		self.Payment = self.Hold + p.Pass

