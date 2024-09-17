# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseFixedDiscountAmount(http.Controller):
#     @http.route('/purchase_fixed_discount_amount/purchase_fixed_discount_amount', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_fixed_discount_amount/purchase_fixed_discount_amount/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_fixed_discount_amount.listing', {
#             'root': '/purchase_fixed_discount_amount/purchase_fixed_discount_amount',
#             'objects': http.request.env['purchase_fixed_discount_amount.purchase_fixed_discount_amount'].search([]),
#         })

#     @http.route('/purchase_fixed_discount_amount/purchase_fixed_discount_amount/objects/<model("purchase_fixed_discount_amount.purchase_fixed_discount_amount"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_fixed_discount_amount.object', {
#             'object': obj
#         })

