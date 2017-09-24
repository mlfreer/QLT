from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):
	def is_displayed(self):
		return self.player.subsession.round_number == 1
	template_name = 'UGGARP/Welcome.html'

class ProposerDecision(Page):
	template_name = 'UGGARP/Proposer.html'
	form_model = models.Player
	form_fields = ['proposers_choice']
	def vars_for_template(self):
		return {
		'proposer_earning_a': Constants.proposer_earnings['a'][self.subsession.round_number-1],
		'responder_earning_a': Constants.responder_earnings['a'][self.subsession.round_number-1],
		'proposer_earning_b': Constants.proposer_earnings['b'][self.subsession.round_number-1],
		'responder_earning_b': Constants.responder_earnings['b'][self.subsession.round_number-1],
		'proposer_earning_c': Constants.proposer_earnings['c'][self.subsession.round_number-1],
		'responder_earning_c': Constants.responder_earnings['c'][self.subsession.round_number-1],
		'proposer_earning_d': Constants.proposer_earnings['d'][self.subsession.round_number-1],
		'responder_earning_d': Constants.responder_earnings['d'][self.subsession.round_number-1],
		'proposer_earning_e': Constants.proposer_earnings['e'][self.subsession.round_number-1],
		'responder_earning_e': Constants.responder_earnings['e'][self.subsession.round_number-1],
		'proposer_earning_f': Constants.proposer_earnings['f'][self.subsession.round_number-1],
		'responder_earning_f': Constants.responder_earnings['f'][self.subsession.round_number-1],
		'proposer_earning_g': Constants.proposer_earnings['g'][self.subsession.round_number-1],
		'responder_earning_g': Constants.responder_earnings['g'][self.subsession.round_number-1],
		'proposer_earning_h': Constants.proposer_earnings['h'][self.subsession.round_number-1],
		'responder_earning_h': Constants.responder_earnings['h'][self.subsession.round_number-1],
		'proposer_earning_i': Constants.proposer_earnings['i'][self.subsession.round_number-1],
		'responder_earning_i': Constants.responder_earnings['i'][self.subsession.round_number-1],
		'proposer_earning_j': Constants.proposer_earnings['j'][self.subsession.round_number-1],
		'responder_earning_j': Constants.responder_earnings['j'][self.subsession.round_number-1],
		'proposer_earning_k': Constants.proposer_earnings['k'][self.subsession.round_number-1],
		'responder_earning_k': Constants.responder_earnings['k'][self.subsession.round_number-1],
		'proposer_earning_l': Constants.proposer_earnings['l'][self.subsession.round_number-1],
		'responder_earning_l': Constants.responder_earnings['l'][self.subsession.round_number-1],
		'proposer_earning_m': Constants.proposer_earnings['m'][self.subsession.round_number-1],
		'responder_earning_m': Constants.responder_earnings['m'][self.subsession.round_number-1]
		}

class ResponderDecision(Page):
	template_name = 'UGGARP/Responder.html'
	form_model = models.Player
	form_fields = ['responders_choice_a','responders_choice_b','responders_choice_c', 'responders_choice_d', 'responders_choice_e','responders_choice_f','responders_choice_g','responders_choice_h','responders_choice_i','responders_choice_j','responders_choice_k','responders_choice_l','responders_choice_m']
	def vars_for_template(self):
		return {
		'proposer_earning_a': Constants.proposer_earnings['a'][self.subsession.round_number-1],
		'responder_earning_a': Constants.responder_earnings['a'][self.subsession.round_number-1],
		'proposer_earning_b': Constants.proposer_earnings['b'][self.subsession.round_number-1],
		'responder_earning_b': Constants.responder_earnings['b'][self.subsession.round_number-1],
		'proposer_earning_c': Constants.proposer_earnings['c'][self.subsession.round_number-1],
		'responder_earning_c': Constants.responder_earnings['c'][self.subsession.round_number-1],
		'proposer_earning_d': Constants.proposer_earnings['d'][self.subsession.round_number-1],
		'responder_earning_d': Constants.responder_earnings['d'][self.subsession.round_number-1],
		'proposer_earning_e': Constants.proposer_earnings['e'][self.subsession.round_number-1],
		'responder_earning_e': Constants.responder_earnings['e'][self.subsession.round_number-1],
		'proposer_earning_f': Constants.proposer_earnings['f'][self.subsession.round_number-1],
		'responder_earning_f': Constants.responder_earnings['f'][self.subsession.round_number-1],
		'proposer_earning_g': Constants.proposer_earnings['g'][self.subsession.round_number-1],
		'responder_earning_g': Constants.responder_earnings['g'][self.subsession.round_number-1],
		'proposer_earning_h': Constants.proposer_earnings['h'][self.subsession.round_number-1],
		'responder_earning_h': Constants.responder_earnings['h'][self.subsession.round_number-1],
		'proposer_earning_i': Constants.proposer_earnings['i'][self.subsession.round_number-1],
		'responder_earning_i': Constants.responder_earnings['i'][self.subsession.round_number-1],
		'proposer_earning_j': Constants.proposer_earnings['j'][self.subsession.round_number-1],
		'responder_earning_j': Constants.responder_earnings['j'][self.subsession.round_number-1],
		'proposer_earning_k': Constants.proposer_earnings['k'][self.subsession.round_number-1],
		'responder_earning_k': Constants.responder_earnings['k'][self.subsession.round_number-1],
		'proposer_earning_l': Constants.proposer_earnings['l'][self.subsession.round_number-1],
		'responder_earning_l': Constants.responder_earnings['l'][self.subsession.round_number-1],
		'proposer_earning_m': Constants.proposer_earnings['m'][self.subsession.round_number-1],
		'responder_earning_m': Constants.responder_earnings['m'][self.subsession.round_number-1]
		}

class ResultsWaitPage(WaitPage):

	form_model = models.Player
	def after_all_players_arrive(self):
		for g in self.subsession.get_groups():
			g.get_player_payment()
		if self.subsession.round_number==Constants.num_rounds:
			for p in self.subsession.get_players():
				p.get_final_payment()


class Results(Page):
	def is_displayed(self):
		return self.player.subsession.round_number == Constants.num_rounds
	def vars_for_template(self):
		return{
		'payment_round': self.group.payment_round,
		'player_in_all_rounds': self.player.in_all_rounds(),
		}


page_sequence = [
	Welcome,
	ProposerDecision,
	ResponderDecision,
	ResultsWaitPage,
	Results
]
