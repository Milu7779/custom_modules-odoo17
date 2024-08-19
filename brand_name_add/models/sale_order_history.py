from odoo import models, fields, api


SALE_ORDER_STATE = [
    ('draft', "Quotation"),
    ('sent', "Quotation Sent"),
    ('sale', "Sales Order"),
    ('cancel', "Cancelled"),
]

class SaleOrderHistory(models.Model):
    _name = 'sale.order.history'
    _description = 'Sale order history'

    sale_order_history_line_id = fields.Many2one(
        comodel_name='sale.order',
        inverse_name='sale_order_history_id',
        string='sale order history')
    re_order = fields.Boolean(string='Re Order')
    sale_order_id = fields.Char(string='sale order')
    order_date = fields.Datetime(string='order date')
    product_name = fields.Many2one('product.product', string='Product')
    price = fields.Float(string='price')
    qty = fields.Integer(string='quantity')
    discount = fields.Float(string='Discount')
    sub_total = fields.Float(string='sub Total')
    order_status = fields.Selection(
        selection=SALE_ORDER_STATE,
        string="Status",
        readonly=True, copy=False, index=True,
        tracking=3,
        default='draft')


    def action_reorder(self):
        if self.sale_order_history_line_id:
            return self.sale_order_history_line_id.action_reorder()
        return False

