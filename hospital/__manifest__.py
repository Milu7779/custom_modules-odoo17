# -*- coding: utf-8 -*-
{
    'name': "Hospital",

    'summary': "Hospital Management",

    'description': """
Hospital Module to manage Doctors and patients
    """,

    'author': "Health",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
         'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/doctors_view.xml',
        'views/patients_view.xml',
        'views/appointments_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

