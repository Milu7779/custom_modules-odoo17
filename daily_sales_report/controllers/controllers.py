# -*- coding: utf-8 -*-
# from odoo import http


# class DailySalesReport(http.Controller):
#     @http.route('/daily_sales_report/daily_sales_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/daily_sales_report/daily_sales_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('daily_sales_report.listing', {
#             'root': '/daily_sales_report/daily_sales_report',
#             'objects': http.request.env['daily_sales_report.daily_sales_report'].search([]),
#         })

#     @http.route('/daily_sales_report/daily_sales_report/objects/<model("daily_sales_report.daily_sales_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('daily_sales_report.object', {
#             'object': obj
#         })

