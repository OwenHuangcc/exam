{
    'name': 'exam測試',
    'description': """test""",
    'summary': 'testtest',
    'version': '1.0.0',
    'category': 'Uncategory',
    'author': 'Test小明',
    'depends': ['base','purchase'],
    'data': [
        'security/ir.model.access.csv',
        'security/group_buying_security.xml',
        'views/view_action.xml',
        'data/sequence.xml',
        'views/idx_purchase.xml',
        'views/group_buying.xml',
        'views/view_menuitem.xml',

    ],
    'license': 'Other proprietary',
    'installable': True,
    'application': True,
    'auto_install': False,
}
