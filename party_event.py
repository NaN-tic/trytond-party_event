#This file is part party_event module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import Pool
from trytond.transaction import Transaction

import datetime

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
    _name = 'party.event'
    _description = __doc__
    _order_name = 'date'

    type = fields.Selection(_TYPES, 'Type', required=True, sort=False)
    event_date = fields.DateTime('Date', required=True)
    subject = fields.Char('Subject', required=True)
    description = fields.Text('Description')
    party = fields.Many2One('party.party', 'Party', required=True)
    resource = fields.Reference('Resource', selection='get_resource')
    user = fields.Many2One('res.user', 'User', required=True)

    def __init__(self):
        super(PartyEvent, self).__init__()
        self._order.insert(0, ('event_date', 'DESC'))
        self._error_messages.update({
            'no_subject': 'No subject',
        })

    def default_type(self):
        return 'email'

    def get_resource(self):
        '''Get Resources. Rewrite this method to add new resource references'''
        res = []
        return res

    def get_rec_name(self, ids, name):
        if not ids:
            return {}
        res = {}
        for mail in self.browse(ids):
            res[mail.id] = mail.subject
        return res

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
            self.create(values)
        except:
            pass
        return True

PartyEvent()
