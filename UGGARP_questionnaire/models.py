from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)


author = 'Mikhail Freer'

doc = """
Questionnaire for Castillo Cross and Freer: Nonparametric Utility Theory... """


class Constants(BaseConstants):
	name_in_url = 'uggarpq'
	players_per_group = None
	num_rounds = 1


class Subsession(BaseSubsession):
	pass


class Group(BaseGroup):
	pass


class Player(BasePlayer):
	Gender = models.CharField(choices=[('M','Male'), ('F','Female')],widget=widgets.RadioSelect())
	Major = models.CharField()
	Age = models.IntegerField(min=18, max=99)
	YearInCollege = models.CharField(choices=[('F','Freshman'), ('So','Sophomore'), ('J','Junior'),('Se','Senior'), ('GS','Graduate Student')], widget=widgets.RadioSelect())
	PreviousParticipation = models.CharField(choices=[('Y','Yes'), ('F','No')],widget=widgets.RadioSelect())
	EconomicsCourses = models.CharField()
	IsAltruistic = models.IntegerField(initial=0)
	BeliefConsistency = models.IntegerField(initial=0)
