# -*- coding: utf-8 -*-
# from odoo import http


# class ProductRestriction(http.Controller):
#     @http.route('/product_restriction/product_restriction', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_restriction/product_restriction/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_restriction.listing', {
#             'root': '/product_restriction/product_restriction',
#             'objects': http.request.env['product_restriction.product_restriction'].search([]),
#         })

#     @http.route('/product_restriction/product_restriction/objects/<model("product_restriction.product_restriction"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_restriction.object', {
#             'object': obj
#         })

