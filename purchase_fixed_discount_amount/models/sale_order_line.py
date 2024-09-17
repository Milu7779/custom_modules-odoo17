from odoo import fields, models, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    purchase_order_lines = fields.Many2many(
        'purchase.order.line',
        string='purchase order lines'
    )
    fixed_discount_amount = fields.Float(
        string='Fixed Discount Amount',
        compute='_compute_fixed_discount_amount',
        store = True
    )

    @api.depends('purchase_order_lines', 'product_id')
    def _compute_fixed_discount_amount(self):
        for line in self:
            matching_purchase_lines = self.env['purchase.order.line'].search([
                ('product_id', '=', line.product_id.id),
                ('fixed_discount_amount', '>', 0.0)
            ])
            discount_amounts = matching_purchase_lines.filtered(lambda pl: pl.product_id == line.product_id)
            if discount_amounts:
                line.fixed_discount_amount = sum(discount_amounts.mapped('fixed_discount_amount'))
            else:
                line.fixed_discount_amount = 0.0