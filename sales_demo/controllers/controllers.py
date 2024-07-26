# -*- coding: utf-8 -*-
# from odoo import http


# class SalesDemo(http.Controller):
#     @http.route('/sales_demo/sales_demo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_demo/sales_demo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_demo.listing', {
#             'root': '/sales_demo/sales_demo',
#             'objects': http.request.env['sales_demo.sales_demo'].search([]),
#         })

#     @http.route('/sales_demo/sales_demo/objects/<model("sales_demo.sales_demo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_demo.object', {
#             'object': obj
#         })

