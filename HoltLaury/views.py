from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Welcome(Page):
	template_name = 'HoltLaury/Welcome.html'

class Decision(Page):
	template_name = 'HoltLaury/Decision.html'
	form_model = models.Player
	form_fields = ['L1','L2','L3','L4','L5','L6','L7','L8','L9','L10']


class ResultsWaitPage(WaitPage):
	wait_for_all_groups=True
	#template_name = 'HoltLaury/Wait.html'
	def after_all_players_arrive(self):
		for p in self.group.get_players():
			p.get_payoff()


class Results(Page):
	template_name = 'HoltLaury/Results.html'
	form_model = models.Player


page_sequence = [
	Welcome,
	Decision,
	ResultsWaitPage
]
