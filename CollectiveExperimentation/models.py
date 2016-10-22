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
		for p in self.get_players():
			p.set_type()
			p.get_mynumber()




class Group(BaseGroup):
	RiskyChosen = models.IntegerField(initial = 0) #is risky alternative chosen
	Votes2Start = models.IntegerField(initial = 0) #the amount of people voted to start (Stage 1)
	Votes2Continue = models.IntegerField(initial = 0) #the amount of people voted to continue experimenting (Stage 2)
	Votes2Implement = models.IntegerField(initial = 0) #the amount of people voted to implement RA (Stage 3)

	def count_votes2start(self):
		for p in self.get_players():
			p.get_vote_stage1()
			self.Votes2Start = self.Votes2Start + p.VoteStage1

	def count_votes2continue(self):
		for p in self.get_players():
			p.get_vote_stage2()
			self.Votes2Continue = self.Votes2Continue + p.VoteStage2

	def count_votes2implement(self):
		for p in self.get_players():
			p.get_vote_stage3()
			self.Votes2Implement = self.Votes2Implement + p.VoteStage3

	#determining the group decisions at every stage
	Start = models.IntegerField(initial=0) #whether group wants to start
	Continue = models.IntegerField(initial=0) #whether group wants to contiue
	Implement = models.IntegerField(initial=0) #whether group wants to implement

	def get_start(self):
		self.count_votes2start()
		if self.Votes2Start>=2:
			self.Start = 1

	def get_continue(self):
		self.count_votes2continue()
		if self.Votes2Continue>=2:
			self.Continue = 1

	def get_implement(self):
		self.count_votes2implement()
		if self.Votes2Implement>=2:
			self.Implement = 1




class Player(BasePlayer):
	Type = models.IntegerField(initial=0) #=type of player: 1 = High, 0 = Low
	def set_type(self):
		r = random.uniform(0,1)
		if r>=Constants.p:
			self.Type=1

	MyNumber = models.IntegerField() #my number in group
	def get_mynumber(self):
		self.MyNumber=self.id_in_group

	Signal1 = models.IntegerField(initial=0) #= signal at the stage 1: 1=High, 0=Uncertain
	Signal2 = models.IntegerField(initial=0) #= signal at the stage 2: 1=High, 0=Uncertain
	#next comes the verbalized versions of signals, for the views
	VerbalSignal1 = models.CharField(choices = ['Uncertain', 'High'])
	VerbalSignal2 = models.CharField(choices=['Uncertain','High'])
	def get_signal1(self):
		r = random.uniform(0,1)
		if (r>=Constants.q) and (self.Type==1):
			self.Signal1=1;
			self.VerbalSignal1='High'
		else:
			self.VerbalSignal1='Uncertain'

	def get_signal2(self):
		r = random.uniform(0,1)
		if (r>=Constants.q) and (self.Type==1):
			self.Signal2=1;
			self.VerbalSignal2='High'
		else:
			self.VerbalSignal2='Uncertain'


	#decision variables: 3 stages of voting
	VoteStage1 = models.IntegerField(initial=0)
	VoteStage2 = models.IntegerField(initial=0)
	VoteStage3 = models.IntegerField(initial=0)
	#verbalized decisions:
	VerbalVoteStage1 = models.CharField(
		choices=['Yes','No'],
		widget=widgets.RadioSelect()
		)
	VerbalVoteStage2 = models.CharField(
		choices=['Yes','No'],
		widget=widgets.RadioSelect()
		)
	VerbalVoteStage3 = models.CharField(
		choices=['Yes','No'],
		widget=widgets.RadioSelect()
		)

	#functions for the player
	def get_vote_stage1(self):
		if self.VerbalVoteStage1 == 'Yes':
			self.VoteStage1=1

	def get_vote_stage2(self):
		if self.VerbalVoteStage2 == 'Yes':
			self.VoteStage2=1

	def get_vote_stage3(self):
		if self.VerbalVoteStage3 == 'Yes':
			self.VoteStage1=3

	#determining the payoff of player
	Payment = models.IntegerField(initial=Constants.Safe)
	
	def get_payoff(self):
		if self.group.Implement==1:
			if self.Type == 1:
				self.Payment = Constants.High
			else:
				self.Payment = Constants.Low
