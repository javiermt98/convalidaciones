# -*- coding: utf-8 -*-
{
    'name': "convalidaciones",

    'summary': """Aplicación de convalidaciones""",

    'description': """
        Práctica de una aplicación de convalidaciones de módulos en un instituto
    """,

    'author': "Javier Máñez",
    'website': "nowebsite.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/alumno_view.xml',
        'views/ciclo_view.xml',
        'views/conv_view.xml',
        'views/modulo_view.xml',
        'views/profesor_view.xml',
        'views/templates.xml',
        'views/menu_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
