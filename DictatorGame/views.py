from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Decision(Page):
	template_name = 'DictatorGame/Decision.html'
	form_model = models.Player
	form_fields = ['Pass']



class ResultsWaitPage(WaitPage):

	def after_all_players_arrive(self):
		self.group.compute_payments()


class Results(Page):
	template_name = 'DictatorGame/Results.html'


page_sequence = [
	Decision,
	ResultsWaitPage,
	Results
]
