{
    'name': 'CRM Team Lead',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Module to add Team Lead user group in CRM',
    'author': 'Your Name',
    'depends': ['crm'],
    'data': [
        'security/ir.model.access.csv',
        'security/crm_team_security.xml',
        'views/crm_team_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}