from odoo import fields, models, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    fixed_discount_amount = fields.Float(
        string='Fixed Discount Amount'
    )

    @api.onchange('fixed_discount_amount','product_id')
    def _onchange_fixed_discount_amount(self):
        #super(PurchaseOrderLine)._compute_amount()
        if self.fixed_discount_amount:

            #untaxed case
            subtotal = (self.product_qty * self.price_unit)/ self.fixed_discount_amount
            total = subtotal
            self.price_subtotal = subtotal
            self.price_total = total





