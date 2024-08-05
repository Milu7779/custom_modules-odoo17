# -*- coding: utf-8 -*-
# from odoo import http


# class HospitalManagement(http.Controller):
#     @http.route('/hospital__management/hospital__management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital__management/hospital__management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital__management.listing', {
#             'root': '/hospital__management/hospital__management',
#             'objects': http.request.env['hospital__management.hospital__management'].search([]),
#         })

#     @http.route('/hospital__management/hospital__management/objects/<model("hospital__management.hospital__management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital__management.object', {
#             'object': obj
#         })

