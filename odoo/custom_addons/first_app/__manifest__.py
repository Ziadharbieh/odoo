{
    'name': "ziad",
    'author': "ziad harbieh", 
    'version': "18.0.0.1",
    'category': "Custom",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
    ],
    'application': True,
    'installable': True,
    'assets': {
        'web.assets_backend': [
        ],
    }
}