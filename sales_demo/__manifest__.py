# -*- coding: utf-8 -*-
{
    'name': "sales_demo",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.4',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','sale_management','product'],

    # always loaded
    'data': [
         'security/ir.model.access.csv',
        'views/sales_inherit_view.xml',
        #'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

