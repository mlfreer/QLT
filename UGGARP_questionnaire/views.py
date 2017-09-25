from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):
	template_name = 'UGGARP/Welcome.html'


class Questions(Page):
	template_name = 'UGGARP/Questions.html'
	form_model = models.Player
	form_fields = ['Gender','Major','Age','YearInCollege','PreviousParticipation','EconomicsCourses','IsAltruistic','BeliefConsistency']

class Final(Page):
	template_name = 'UGGARP/Final.html'


page_sequence = [
	Welcome,
	Questions,
	Final
]
