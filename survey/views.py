# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants

class Survey(Page):

    template_name = 'survey_sample/Survey.html'

    form_model = models.Player
    form_fields = ['q_gender']


page_sequence = [Survey]