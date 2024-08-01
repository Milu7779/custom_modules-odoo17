# -*- coding: utf-8 -*-
{
    'name': "sale_inventory_brand",

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
    'depends': ['sale','sale_management','stock','stock_account','sales_demo'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order_template.xml',
        'views/stock_picking_templates.xml',
        'views/stock_move_template.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

