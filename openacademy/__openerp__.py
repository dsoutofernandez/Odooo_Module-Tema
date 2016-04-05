# -*- coding: utf-8 -*-
{
    'name': "openacademy1",

    'summary': """
        Este es el modulo para el examen""",

    'description': """
        Modulo y tema Odoo examen
    """,

    'author': "dsoutofernandez",
    'website': "http://www.danielcastelao.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}