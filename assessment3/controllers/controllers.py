# -*- coding: utf-8 -*-
# from odoo import http


# class Assessment3(http.Controller):
#     @http.route('/assessment3/assessment3', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/assessment3/assessment3/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('assessment3.listing', {
#             'root': '/assessment3/assessment3',
#             'objects': http.request.env['assessment3.assessment3'].search([]),
#         })

#     @http.route('/assessment3/assessment3/objects/<model("assessment3.assessment3"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('assessment3.object', {
#             'object': obj
#         })

