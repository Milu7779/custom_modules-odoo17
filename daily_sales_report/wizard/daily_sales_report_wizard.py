from odoo import models, fields, api
from odoo import http
from odoo.http import request

class DailySalesReportWizard(models.TransientModel):
    _name = 'daily.sales.report.wizard'

    sale_order_ids = fields.Many2many(
        'sale.order',
        default=lambda self: self.env.context.get('active_id')
    )
    date_from = fields.Date(
        string="Date From"
    )
    date_to = fields.Date(
        string=" Date To"
    )
    sales_person = fields.Many2one(
        'res.users',
        string='Sales Person'
    )

    def action_generate_report(self):

        sale_orders = self.env['sale.order'].search([
            ('date_order', '>=', self.date_from),
            ('date_order', '<=', self.date_to),
            ('user_id', '=', self.sales_person.id)
        ])
        print('orders..',sale_orders)
        for line in sale_orders:
            print('name=',line.name)

        report_data = {
            'date_from': self.date_from,
            'date_to': self.date_to,
            'sales_person_name': self.sales_person.name,
            'sale_orders': sale_orders.ids,
        }
        print('data',report_data)

        return self.env.ref('daily_sales_report.action_daily_sales_report_pdf').report_action(self,  data=report_data)


