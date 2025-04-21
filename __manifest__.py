{
    'name': 'CRM Team Lead',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Module to add Team Lead user group in CRM',
    'author': 'Your Name',
    'depends': ['crm'],
    'data': [
        'security/crm_team_security.xml',
        'security/ir.model.access.csv',
        'views/crm_team_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}