# -*- coding: utf-8 -*-
# from odoo import http


# class BrandNameAdd(http.Controller):
#     @http.route('/brand_name_add/brand_name_add', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/brand_name_add/brand_name_add/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('brand_name_add.listing', {
#             'root': '/brand_name_add/brand_name_add',
#             'objects': http.request.env['brand_name_add.brand_name_add'].search([]),
#         })

#     @http.route('/brand_name_add/brand_name_add/objects/<model("brand_name_add.brand_name_add"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('brand_name_add.object', {
#             'object': obj
#         })

