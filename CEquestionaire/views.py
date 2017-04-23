from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Questionnaire(Page):
	template_name = 'CEquestionaire/Q.html'
	form_model = models.Player
	form_fields = ['Gender','Age','NumOfSiblings','Ethnicity','Experienced','YearInCollege','GPA','Major']
	def GPA_min(self):
		return 0.00
	def GPA_max(self):
		return 4.00
		


class FinalPage(Page):
	template_name = 'CEquestionaire/Final.html'

page_sequence = [
	Questionnaire,
	FinalPage
]
