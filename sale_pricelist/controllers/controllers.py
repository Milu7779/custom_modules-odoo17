# -*- coding: utf-8 -*-
# from odoo import http


# class SalePricelist(http.Controller):
#     @http.route('/sale_pricelist/sale_pricelist', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_pricelist/sale_pricelist/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_pricelist.listing', {
#             'root': '/sale_pricelist/sale_pricelist',
#             'objects': http.request.env['sale_pricelist.sale_pricelist'].search([]),
#         })

#     @http.route('/sale_pricelist/sale_pricelist/objects/<model("sale_pricelist.sale_pricelist"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_pricelist.object', {
#             'object': obj
#         })

