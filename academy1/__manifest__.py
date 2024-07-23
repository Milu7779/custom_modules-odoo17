# -*- coding: utf-8 -*-
{
    'name': "academy 2024",
    'summary': "Manage teachers and students data",

    'description': """
Academy module to manage Teachers And Students detailes
    """,

    'author': "Education",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.3',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
         'security/ir.model.access.csv',
        'views/students_view.xml',
        'views/teachers_view.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

