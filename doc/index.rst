Party Event Module
##################

The party_event module add events (history communication) in party. For example, you have all emails, calls, ... to this party.

Events is only read mode. To add new events, use extra modules, eg electronic_mail_event.

To add events you can call create_event method:

- party: party ID
- resource: str (object,id) Eg: 'electrinic.mail,1'
- values: Dicc {subject:, date:, description:} (optional)

Example:

from trytond.pool import Pool

party = party_id
resource = 'electronic.mail,%s' % email_id
values = {
    'subject':'This is example event party',
    'description':'Congragulations! Party event save!',
}
Pool().get('party.event').create_event(party, resource, values)
