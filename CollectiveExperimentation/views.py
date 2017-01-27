# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants

#first decision stage
class WelcomePage(Page):
	template_name ='CollectiveExperimentation/Welcome.html'

class Decision2Start(Page):
	form_model = models.Player
	form_fields = ['VerbalVoteStage1']

	template_name = 'CollectiveExperimentation/Decision2Start.html'

class Signals1WaitPage(WaitPage):
	def after_all_players_arrive(self):
		self.group.get_start()
		for p in self.group.get_players():
			p.get_signal1()

		
	template_name = 'CollectiveExperimentation/Signals1WaitPage.html'

class Decision2Continue(Page):

	def is_displayed(self):
		return self.player.group.Start

	form_model = models.Player
	form_fields = ['VerbalVoteStage2']

	template_name = 'CollectiveExperimentation/Decision2Continue.html'

class Signals2WaitPage(WaitPage):
	def is_displayed(self):
		return self.player.group.Start

	def after_all_players_arrive(self):
		self.group.get_continue()
		for p in self.group.get_players():
			p.get_signal2()


	template_name = 'CollectiveExperimentation/Signals1WaitPage.html'


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

	template_name = 'CollectiveExperimentation/Signals1WaitPage.html'



class Results(Page):
	pass


page_sequence = [
	WelcomePage,
	Decision2Start,
	Signals1WaitPage,
	Decision2Continue,
	Signals2WaitPage,
	Decision2Implement,
	ResultsWaitPage,
	Results
]
