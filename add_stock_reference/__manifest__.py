# -*- coding: utf-8 -*-
{
    'name': "add_stock_reference",

    'summary': "add stock_preference field in sale.order to stock.picking",

    'description': """
Add new field
    """,
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','sale','stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/add_stock_reference.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}

