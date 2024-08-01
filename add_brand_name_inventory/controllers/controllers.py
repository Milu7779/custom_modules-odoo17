# -*- coding: utf-8 -*-
# from odoo import http


# class SaleInventoryBrand(http.Controller):
#     @http.route('/sale_inventory_brand/sale_inventory_brand', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_inventory_brand/sale_inventory_brand/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_inventory_brand.listing', {
#             'root': '/sale_inventory_brand/sale_inventory_brand',
#             'objects': http.request.env['sale_inventory_brand.sale_inventory_brand'].search([]),
#         })

#     @http.route('/sale_inventory_brand/sale_inventory_brand/objects/<model("sale_inventory_brand.sale_inventory_brand"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_inventory_brand.object', {
#             'object': obj
#         })

