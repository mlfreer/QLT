# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants

import random

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

class ResultsWaitPage(WaitPage):
	template_name = 'choistorr/WaitPage.html' 

	


class Results(Page):
	form_model = models.Player
	template_name = 'choistorr/Results.html'
    


page_sequence = [
    Prediction,
    Decision,
    ResultsWaitPage,
    Results
]
