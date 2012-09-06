#This file is part party_event module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
{
    'name': 'Party Event',
    'name_ca_ES': 'Historial de tercers',
    'name_es_ES': 'Historial de terceros',
    'version': '2.4.0',
    'author': 'Zikzakmedia',
    'email': 'zikzak@zikzakmedia.com',
    'website': 'http://www.zikzakmedia.com/',
    'description': '''History party communication. Extra modules add events''',
    'description_ca_ES': '''Historial de comunicació de tercers. Moduls extres afegeixen els esdeveniments''',
    'description_es_ES': '''Historial de comunicación de terceros. Módulos externos añaden los eventos''',
    'depends': [
        'ir',
        'res',
        'party',
    ],
    'xml': [
        'party_event.xml',
        'party.xml',
    ],
    'translation': [
        'locale/ca_ES.po',
        'locale/es_ES.po',
    ]
}
