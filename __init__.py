#This file is part party_event module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.pool import Pool
from .party_event import *
from .party import *

def register():
    Pool.register(
        PartyEvent,
        Party,
        module='party_event', type_='model')
