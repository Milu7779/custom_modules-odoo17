# -*- coding: utf-8 -*-
{
    'name': "purchase_fixed_discount_amount",

    'summary': "fixed discount amount,sub total,total",

    'description': """
Fixed discount amount reflected in price_subtotal and price_total fields,
Fixed discount amount added sale order report
    """,

    'author': "Amzsys technology pvt Lmtd",
    'website': "https://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','purchase','sale'],

    'data': [
        # 'security/ir.model.access.csv',
        'security/purchase_security.xml',
        'views/purchase_order_view.xml',
        'views/sale_order_view.xml',
        'views/sale_portal_template.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}

