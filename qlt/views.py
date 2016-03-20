# -*- coding: utf-8 -*-
from __future__ import division

import decimal
from otree.common import Currency as c, currency_range, safe_json
from django import forms
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Decision(Page):
    #CashQuantity = forms.DecimalField(initial=0)
    def is_displayed(self):
    	return self.player.subsession.round_number <= Constants.num_rounds

    form_model = models.Player
    form_fields = ['CashQuantity','MasonMoneyQuantity','BarnesNobleQuantity','FandangoQuantity','GapQuantity']
    
    def CashQuantity_choices(self):
    	return range(0,int(100/self.player.CashPrice)+1,1)

    def MasonMoneyQuantity_choices(self):
    	return [i for j in (range(0,1,1), range(5,int(100/self.player.MasonMoneyPrice)+1,1)) for i in j]

    def FandangoQuantity_choices(self):
    	return [0, 15, 25, 35]

    def BarnesNobleQuantity_choices(self):
    	
    	return [i for j in (range(0,1,1), range(10,int(100/self.player.BarnesNoblePrice)+1,1)) for i in j]#

    def GapQuantity_choices(self):
    	return [i for j in (range(0,1,1), range(10,int(100/self.player.GapPrice)+1,1)) for i in j]

    template_name = 'qlt/Decision.html'

    def vars_for_template(self):
    	return{
    	'CashSpending': decimal.Decimal(self.player.CashQuantity)*self.player.CashPrice,
    	'MasonMoneySpending': decimal.Decimal(self.player.MasonMoneyQuantity)*self.player.MasonMoneyPrice,
    	'BarnesNobleSpending': decimal.Decimal(self.player.BarnesNobleQuantity)*self.player.BarnesNoblePrice,
    	'FandangoSpending': decimal.Decimal(self.player.FandangoQuantity)*self.player.FandangoPrice,
    	'GapSpending': decimal.Decimal(self.player.GapQuantity)*self.player.GapPrice,
    	'Expenditure': self.player.Expenditure,

    	}

    def before_next_page(self):
        self.player.compute_spendings()

    def error_message(self,values):
        self.player.BarnesNobleQuantity=values["BarnesNobleQuantity"]
        self.player.FandangoQuantity=values["FandangoQuantity"]
        self.player.GapQuantity=values["GapQuantity"]
        self.player.CashQuantity=values["CashQuantity"]
        self.player.MasonMoneyQuantity=values["MasonMoneyQuantity"]
        self.player.Expenditure=values["CashQuantity"]*self.player.CashPrice+values["MasonMoneyQuantity"]*self.player.MasonMoneyPrice+values["BarnesNobleQuantity"]*self.player.BarnesNoblePrice+values["FandangoQuantity"]*self.player.FandangoPrice+values["GapQuantity"]*self.player.GapPrice
        self.player.compute_spendings()
        self.player.compute_spendings()
        if (self.player.Expenditure > 100):
            return 'Your Expenditures must not exceed 100 tokens'

        cq = self.player.CashPrice
        
        if self.player.MasonMoneyQuantity>=5:
            cmm = self.player.MasonMoneyPrice
        else:
            cmm = 5*self.player.MasonMoneyPrice

        if self.player.GapQuantity>=10:
            cg = self.player.GapPrice
        else:
            cg = 10*self.player.GapPrice

        if self.player.BarnesNobleQuantity>=10:
            cbn = self.player.BarnesNoblePrice
        else:
            cbn = 10*self.player.BarnesNoblePrice

        min_incr = min(cg,cmm,cq,cbn)


        if (100-self.player.Expenditure >= min_incr):
            return 'You can buy more goods at given prices'

class ResultsWaitPage(WaitPage):
	def is_displayed(self):
		return self.player.subsession.round_number == Constants.num_rounds

	def after_all_players_arrive(self):
		pass

	template_name = 'qlt/ResultsWaitingPage.html'


class Questions(Page):
    form_model = models.Player
    form_fields = ["Gender","Age","ShareFood","ShareBooks","ShareCloths","ShareMovies"]

    def error_message(self,values):
        self.player.ShareFood = values["ShareFood"]
        self.player.ShareBooks = values["ShareBooks"]
        self.player.ShareMovies = values["ShareMovies"]
        self.player.ShareCloths = values["ShareCloths"]

        if values["ShareCloths"]+values["ShareMovies"]+values["ShareBooks"]+values["ShareFood"] > 100:
            return 'Your spendings are larger than your income...'


    def is_displayed(self):
        return self.player.subsession.round_number == Constants.num_rounds

    template_name = 'qlt/Questions.html'



class Results(Page):
	def is_displayed(self):
		return self.player.subsession.round_number == Constants.num_rounds

	def vars_for_template(self):
		self.player.compute_spendings()
		return{
		'paying_round': self.session.vars['paying_round'],
		'player_in_all_rounds': self.player.in_all_rounds(),
		}

	template_name = 'qlt/Results.html'


page_sequence = [
    Decision,
    Questions,
    ResultsWaitPage,
    Results
]
