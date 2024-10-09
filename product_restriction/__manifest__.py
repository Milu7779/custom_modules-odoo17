# -*- coding: utf-8 -*-
{
    'name': "product_restriction",

    'summary': "duplicate product restriction,discount limit validation",

    'description': """
find duplicate product on sale_order_line and purchase_order_line,discount limit set both product as well as product category
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','purchase','product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',

        'views/sale_order_line_view.xml',
        'views/views.xml',
        'views/templates.xml',

        'wizard/res_config_setting_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

