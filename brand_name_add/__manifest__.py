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
    'depends': ['base','sale','sale_management', 'stock', 'account','product'],

    # always loaded
    'data': [
         'security/ir.model.access.csv',
        'views/account_move.xml',
        'views/sale_order_template.xml',
        'views/stock_picking_template.xml',
        'views/sale_suggested_product_line.xml',
        'views/sale_settings_config.xml',
        'views/sale_order_history_line.xml',
        'views/views.xml',
        'views/templates.xml',
        'report/report_sale_order_inherit_document.xml',
        'report/sale_order_preview_report_inherited.xml',
        'report/account_move_preview_report_inherited.xml',
        'report/sale_order_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

