# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division
from otree.db import models
import otree.models
from otree import widgets
from otree.common import Currency as c, currency_range
import random
# </standard imports>
from django_countries.fields import CountryField

class Constants:
    name_in_url = 'survey'
    players_per_group = 2
    num_rounds = 1



class Subsession(otree.models.BaseSubsession):

    pass



class Group(otree.models.BaseGroup):

    # <built-in>
    subsession = models.ForeignKey(Subsession)
    # </built-in>


class Player(otree.models.BasePlayer):

    # <built-in>
    group = models.ForeignKey(Group, null=True)
    subsession = models.ForeignKey(Subsession)
    # </built-in>

    q_gender = models.CharField(
    	choices=[('Male'), ('Female')],
    	verbose_name='Please indicate your gender:', 
    	widget=widgets.RadioSelect())
