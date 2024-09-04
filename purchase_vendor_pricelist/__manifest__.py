# -*- coding: utf-8 -*-
{
    'name': "purchase_vendor_pricelist",

    'summary': "Apply Tiered pricing rules on vendor pricelist",

    'description': """
Apply Tiered pricelist rule on vendor pricelist,while create purchase order tiered pricelist rule applied based on selected product with qty
    """,

    'author': "Amzsys technology pvt Lmtd",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','product','purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/product_template_view.xml'
    ],
    'demo': [
        'demo/demo.xml',
    ],
}

