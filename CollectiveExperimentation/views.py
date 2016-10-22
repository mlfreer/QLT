# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants

#first decision stage
class Decision2Start(Page):
	form_model = models.Player
	form_field = ['MyNumber',]

class Signals1WaitPage(WaitPage):
	def after_all_players_arrive(self):
		self.player.group.count_votes2start()
		
	template_name = 'CollectiveExperimentation/Signals1WaitPage.html'

#getting the first set of public signals
class Signals1(Page):
	pass

class Decision2Continue(Page):
	pass

class Signals2WaitPage(WaitPage):
	def after_all_players_arrive(self):
		self.player.group.count_votes2continue()

	template_name = 'CollectiveExperimentation/Signals1WaitPage.html'

#getting the second set of public signals
class Signals2(Page):
	pass

#deciding whether to implement
class Decision2Implement(Page):
	pass


class ResultsWaitPage(WaitPage):

	def after_all_players_arrive(self):
		self.player.group.count_votes2implement()

	template_name = 'CollectiveExperimentation/Signals1WaitPage.html'



class Results(Page):
	pass


page_sequence = [
	Decision2Start,
	Signals1WaitPage,
	Signals1,
	Decision2Continue,
	Signals2WaitPage,
	Signals2,
	Decision2Implement,
	ResultsWaitPage,
	Results
]
