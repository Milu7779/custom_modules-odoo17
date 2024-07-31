# -*- coding: utf-8 -*-
# from odoo import http


# class AddStockReference(http.Controller):
#     @http.route('/add_stock_reference/add_stock_reference', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/add_stock_reference/add_stock_reference/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('add_stock_reference.listing', {
#             'root': '/add_stock_reference/add_stock_reference',
#             'objects': http.request.env['add_stock_reference.add_stock_reference'].search([]),
#         })

#     @http.route('/add_stock_reference/add_stock_reference/objects/<model("add_stock_reference.add_stock_reference"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('add_stock_reference.object', {
#             'object': obj
#         })

