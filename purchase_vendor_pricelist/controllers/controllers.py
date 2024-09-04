# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseVendorPricelist(http.Controller):
#     @http.route('/purchase_vendor_pricelist/purchase_vendor_pricelist', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_vendor_pricelist/purchase_vendor_pricelist/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_vendor_pricelist.listing', {
#             'root': '/purchase_vendor_pricelist/purchase_vendor_pricelist',
#             'objects': http.request.env['purchase_vendor_pricelist.purchase_vendor_pricelist'].search([]),
#         })

#     @http.route('/purchase_vendor_pricelist/purchase_vendor_pricelist/objects/<model("purchase_vendor_pricelist.purchase_vendor_pricelist"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_vendor_pricelist.object', {
#             'object': obj
#         })

