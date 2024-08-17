from odoo import models, fields, api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    brand_id = fields.Many2one('product.brand', string='Brand')
    serial_no_id = fields.Many2one('stock.lot', string='Serial_number')


class AccountSuggestedLine(models.Model):
    _name = 'account.suggested.line'

    suggest_line_ids = fields.Many2one(comodel_name='account.move', inverse_name='account_sugested_line', string='Suggested Product Lines')
    #suggested_line_ids = fields.Many2many('sale.suggested.line', 'invoice_line_ids',string='Sales suggested product Lines')

    product_id = fields.Many2one('product.product', string='Product')
    product_qty = fields.Integer(string='Quantity')
    product_unit_price = fields.Float(string='Unit Price')
    total_amount = fields.Float(string="Total", compute='_compute_total_amount', store=True)

    @api.depends('product_qty', 'product_unit_price')
    def _compute_total_amount(self):
        for record in self:
            record.total_amount = record.product_qty * record.product_unit_price