from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Welcome(Page):
	template_name = 'DictatorGame/Welcome.html'

class Decision(Page):
	template_name = 'DictatorGame/Decision.html'
	form_model = models.Player
	form_fields = ['Pass']
	def Pass_max(self):
		return 40
	def Pass_min(self):
		return 0



class ResultsWaitPage(WaitPage):
	#template_name = 'DictatorGame/Welcome.html'
	def after_all_players_arrive(self):
		self.subsession.compute_payments()


class Results(Page):
	template_name = 'DictatorGame/Results.html'


page_sequence = [
	Welcome,
	Decision,
	ResultsWaitPage
]
