# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from django import forms

from . import models
from ._builtin import Page, WaitPage
from .models import Constants

import random

class Welcome(Page):
	template_name = 'choistorr/Welcome.html'

	def is_displayed(self):
		return self.player.subsession.round_number == 1

class Prediction(Page):
	form_model = models.Player
	form_fields = ['forecast']

	

	template_name = 'choistorr/Prediction.html'

class Decision(Page):
	form_model = models.Player
	form_fields = ['action']

	template_name = 'choistorr/Decision.html' 

	def before_next_page(self):
		self.player.subsession.determine_round_end() 
		self.player.subsession.compute_next_round() 

class ResultsWaitPage(WaitPage):
	template_name = 'choistorr/WaitPage.html' 


	wait_for_all_groups = True

	def after_all_players_arrive(self):
		self.group.find_y_choosers()
		self.group.set_payoffs()



class Results(Page):
	form_model = models.Player
	

	template_name = 'choistorr/Results.html'
    


page_sequence = [
	Welcome,
    Prediction,
    Decision,
    ResultsWaitPage,
    Results
]
