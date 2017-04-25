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
Holt Laury Risk Preference Test"""


class Constants(BaseConstants):
	name_in_url = 'HoltLaury'
	players_per_group = None
	num_rounds = 1


class Subsession(BaseSubsession):
	pass


class Group(BaseGroup):
	pass


class Player(BasePlayer):
	#choices over 10 HL lotteries, ==1 if option A is chosen, ==0 otherwise
	L1 = models.IntegerField(default=0)
	L2 = models.IntegerField(default=0)
	L3 = models.IntegerField(default=0)
	L4 = models.IntegerField(default=0)
	L5 = models.IntegerField(default=0)
	L6 = models.IntegerField(default=0)
	L7 = models.IntegerField(default=0)
	L8 = models.IntegerField(default=0)
	L9 = models.IntegerField(default=0)
	L10 = models.IntegerField(default=0)


	Payment = models.IntegerField(default=0)
	number_of_lottery = models.IntegerField(default=0)
	optionA = models.IntegerField(default=0)


	def get_payoff(self):
		self.number_of_lottery = random.randint(1,10)
		random_number = random.random()

		if random_number <= self.number_of_lottery/10:
			self.optionA=1

		
		if self.number_of_lottery == 1: 
			self.Payment = self.L1*(40*self.optionA+32*(1-self.optionA))+(1-self.L1)*(77*self.optionA+2*(1-self.optionA))
		if self.number_of_lottery == 2: 
			self.Payment = self.L2*(40*self.optionA+32*(1-self.optionA))+(1-self.L2)*(77*self.optionA+2*(1-self.optionA))
		if self.number_of_lottery == 3: 
			self.Payment = self.L3*(40*self.optionA+32*(1-self.optionA))+(1-self.L3)*(77*self.optionA+2*(1-self.optionA))
		if self.number_of_lottery == 4: 
			self.Payment = self.L4*(40*self.optionA+32*(1-self.optionA))+(1-self.L4)*(77*self.optionA+2*(1-self.optionA))
		if self.number_of_lottery == 5: 
			self.Payment = self.L5*(40*self.optionA+32*(1-self.optionA))+(1-self.L5)*(77*self.optionA+2*(1-self.optionA))
		if self.number_of_lottery == 6: 
			self.Payment = self.L6*(40*self.optionA+32*(1-self.optionA))+(1-self.L6)*(77*self.optionA+2*(1-self.optionA))
		if self.number_of_lottery == 7: 
			self.Payment = self.L7*(40*self.optionA+32*(1-self.optionA))+(1-self.L7)*(77*self.optionA+2*(1-self.optionA))
		if self.number_of_lottery == 8: 
			self.Payment = self.L8*(40*self.optionA+32*(1-self.optionA))+(1-self.L8)*(77*self.optionA+2*(1-self.optionA))
		if self.number_of_lottery == 9: 
			self.Payment = self.L9*(40*self.optionA+32*(1-self.optionA))+(1-self.L9)*(77*self.optionA+2*(1-self.optionA))
		if self.number_of_lottery == 10: 
			self.Payment = self.L10*(40*self.optionA+32*(1-self.optionA))+(1-self.L10)*(77*self.optionA+2*(1-self.optionA))
		





