# -*- coding: utf-8 -*-
# from odoo import http


# class Academy1(http.Controller):
#     @http.route('/academy1/academy1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/academy1/academy1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('academy1.listing', {
#             'root': '/academy1/academy1',
#             'objects': http.request.env['academy1.academy1'].search([]),
#         })

#     @http.route('/academy1/academy1/objects/<model("academy1.academy1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('academy1.object', {
#             'object': obj
#         })

