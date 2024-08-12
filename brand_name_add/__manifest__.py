# -*- coding: utf-8 -*-
{
    'name': "brand_name_add",

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
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale','sale_management', 'stock', 'account'],

    # always loaded
    'data': [
         'security/ir.model.access.csv',
        'views/account_move.xml',
        'views/sale_order_template.xml',
        'views/stock_picking_template.xml',
        'views/views.xml',
        'views/templates.xml',
        'report/report_sale_order_inherit_document.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

