# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants

#first decision stage
class WelcomePage(Page):
	template_name ='CollectiveExperimentation/Welcome.html'
	def is_displayed(self):
		return self.player.subsession.round_number == 1

class Decision2Start(Page):
	form_model = models.Player
	form_fields = ['VerbalVoteStage1']

	template_name = 'CollectiveExperimentation/Decision2Start.html'

class Signals1WaitPage(WaitPage):
	wait_for_all_groups = True
	def after_all_players_arrive(self):
		self.subsession.get_start()
		for p in self.group.get_players():
			p.get_signal1()
			print('*******p.signal1 is', p.Signal1)
			if p.round_number==Constants.num_rounds:
				p.group.set_payment_round()
	
	#template_name = 'CollectiveExperimentation/Signals1WaitPage.html'

class Decision2Continue(Page):

	def is_displayed(self):
		return self.player.group.Start

	form_model = models.Player
	form_fields = ['VerbalVoteStage2']

	template_name = 'CollectiveExperimentation/Decision2Continue.html'

class Signals2WaitPage(WaitPage):

	def after_all_players_arrive(self):
		self.group.get_continue()
		for p in self.group.get_players():
			p.get_signal2()


	#template_name = 'CollectiveExperimentation/Signals1WaitPage.html'


#deciding whether to implement
class Decision2Implement(Page):
	def is_displayed(self):
		return self.player.group.Continue

	form_model = models.Player
	form_fields = ['VerbalVoteStage3']

	template_name = 'CollectiveExperimentation/Decision2Implement.html'

class ResultsWaitPage(WaitPage):

	def after_all_players_arrive(self):
		self.group.get_implement()
		for p in self.group.get_players():
			p.get_payoff()

	#template_name = 'CollectiveExperimentation/Signals1WaitPage.html'



class Results(Page):
	template_name = 'CollectiveExperimentation/Results.html'

class BetweenRounds(WaitPage):
	wait_for_all_groups=True
	#template_name = 'CollectiveExperimentation/Signals1WaitPage.html'

page_sequence = [
	WelcomePage,
	Decision2Start,
	Signals1WaitPage,
	Decision2Continue,
	Signals2WaitPage,
	Decision2Implement,
	ResultsWaitPage,
	Results,
	BetweenRounds
]
