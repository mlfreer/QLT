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
	Gender = models.IntegerField()
	Major = models.CharField()
	Age = models.IntegerField(min=18, max=99)
	YearInCollege = models.IntegerField()
	PreviousParticipation = models.IntegerField()
	EconomicsCourses = models.CharField()
	OtherEconomicsCourse = models.CharField(default=' ')
	IsAltruistic = models.IntegerField(initial=0)
	BeliefConsistency = models.IntegerField(initial=0)
