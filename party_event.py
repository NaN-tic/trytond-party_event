#This file is part party_event module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.transaction import Transaction

import datetime

__all__ = ['PartyEvent']

_TYPES = [
    ('phone', 'Phone'),
    ('mobile', 'Mobile'),
    ('fax', 'Fax'),
    ('email', 'E-Mail'),
    ('skype', 'Skype'),
    ('irc', 'IRC'),
    ('jabber', 'Jabber'),
    ('other', 'Other'),
]

class PartyEvent(ModelSQL, ModelView):
    'Party Event'
    __name__ = 'party.event'
    _order_name = 'date'

    type = fields.Selection(_TYPES, 'Type', required=True, sort=False)
    event_date = fields.DateTime('Date', required=True)
    subject = fields.Char('Subject', required=True)
    description = fields.Text('Description')
    party = fields.Many2One('party.party', 'Party', required=True)
    resource = fields.Reference('Resource', selection='get_resource')
    user = fields.Many2One('res.user', 'User', required=True)

    @classmethod
    def __setup__(cls):
        super(PartyEvent, cls).__setup__()
        cls._order.insert(0, ('event_date', 'DESC'))
        cls._error_messages.update({
            'no_subject': 'No subject',
        })

    @staticmethod
    def default_type():
        return 'email'

    @staticmethod
    def default_event_date():
        return datetime.datetime.now()

    @staticmethod
    def default_user():
        return Transaction().user

    @classmethod
    def get_resource(cls):
        'Return list of Model names for resource Reference'
        return []

    def get_rec_name(self, name):
        return (self.subject or unicode(self.id))

    @classmethod
    def create_event(self, party, resource, values={}):
        """
        Create event at party from details
        :param party: party ID
        :param resource: str (object,id) Eg: 'electrinic.mail,1'
        :param values: Dicc {subject:, date:, description:} (optional)
        """
        now = datetime.datetime.now()
        values = {
            'event_date':values.get('date') or now,
            'subject':values.get('subject') or 
                self.raise_user_error('no_subject',raise_exception=False),
            'description':values.get('description',''),
            'party':party,
            'resource':resource,
            'user':Transaction().user,
        }
        try:
            self.create([values])
        except:
            pass
        return True
