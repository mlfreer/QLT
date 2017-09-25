from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):
	template_name = 'UGGARP_questionnaire/Welcome.html'


class Questions(Page):
	template_name = 'UGGARP_questionnaire/Questions.html'
	form_model = models.Player
	form_fields = ['Gender','Major','Age','YearInCollege','PreviousParticipation','EconomicsCourses','IsAltruistic','BeliefConsistency','OtherEconomicsCourse']

class Final(Page):
	template_name = 'UGGARP_questionnaire/Final.html'


page_sequence = [
	Welcome,
	Questions,
	Final
]
