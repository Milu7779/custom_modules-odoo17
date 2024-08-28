# -*- coding: utf-8 -*-
# from odoo import http


# class SaleProductPricelist(http.Controller):
#     @http.route('/sale_product_pricelist/sale_product_pricelist', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_product_pricelist/sale_product_pricelist/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_product_pricelist.listing', {
#             'root': '/sale_product_pricelist/sale_product_pricelist',
#             'objects': http.request.env['sale_product_pricelist.sale_product_pricelist'].search([]),
#         })

#     @http.route('/sale_product_pricelist/sale_product_pricelist/objects/<model("sale_product_pricelist.sale_product_pricelist"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_product_pricelist.object', {
#             'object': obj
#         })

