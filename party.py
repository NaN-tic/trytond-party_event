#This file is part party_event module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.model import Model, fields

class Party(Model):
    _name = 'party.party'

    events = fields.One2Many('party.event', 'party', 'Events')

Party()
