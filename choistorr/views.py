# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Prediction(Page):
	form_model = models.Player
	form_fields = ['forecast']

	template_name = 'choistorr/Prediction.html'

class Decision(Page):
	form_model = models.Player
	form_fields = ['action']

	template_name = 'choistorr/Decision.html'  

class ResultsWaitPage(WaitPage):
	def after_all_players_arrive(self):
		pass

class Results(Page):
    pass


page_sequence = [
    Prediction,
    Decision,
    ResultsWaitPage,
    Results
]
