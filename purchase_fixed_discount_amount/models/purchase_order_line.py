from odoo import fields, models, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    sale_order_lines = fields.Many2many(
        'sale.order.line',
        string='sale order lines'
    )
    fixed_discount_amount = fields.Float(
        string='Fixed Discount Amount'
    )

    @api.depends('product_qty', 'price_unit', 'taxes_id', 'fixed_discount_amount')
    def _compute_amount(self):
        super(PurchaseOrderLine, self)._compute_amount()

        for line in self:
            discounted_price = line.price_unit - line.fixed_discount_amount
            if line.taxes_id:
                taxes = line.taxes_id.compute_all(
                    discounted_price,
                    line.order_id.currency_id,
                    line.product_qty,
                    product=line.product_id,
                    partner=line.order_id.partner_id
                )
                line.price_subtotal = taxes['total_excluded']
                line.price_total = taxes['total_included']
            else:
                line.price_subtotal = discounted_price * line.product_qty
