from odoo import models, fields, api

class SaleOrderHistory(models.Model):
    _name = 'sale.order.history'
    _description = 'Sale order history'

    sale_order_history_line_id = fields.Many2one(
        comodel_name='sale.order',
        inverse_name='sale_order_history_id',
        string='sale order history')
    sale_order_id = fields.Char(string='sale order')
    order_date = fields.Char(string='')
    product_name = fields.Char(string='Product')