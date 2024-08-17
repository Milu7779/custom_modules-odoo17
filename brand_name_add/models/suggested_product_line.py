
from odoo import models, fields, api

class SaleSuggestedProductLine(models.Model):
    _name = 'sale.suggested.line'


    suggested_product_id = fields.Many2one(comodel_name='sale.order', string='suggested product reference')
    account_suggested_product_id = fields.Many2one(comodel_name='account.move', string='suggested product reference')
    #invoice_line_ids = fields.Many2many('account.suggested.line','suggested_line_ids',string='Sales suggested product Lines')

    product_id = fields.Many2one(comodel_name='product.product', string='Product',domain="[('sale_ok', '=', True)]",options={'no_create': True})
    product_qty = fields.Float(string='Quantity')
    product_unit_price = fields.Float(string='Unit Price')
    total_amount = fields.Float(string="Total", compute='_compute_total_amount', store=True)

    @api.depends('product_qty', 'product_unit_price')
    def _compute_total_amount(self):
        for record in self:
            record.total_amount = record.product_qty * record.product_unit_price