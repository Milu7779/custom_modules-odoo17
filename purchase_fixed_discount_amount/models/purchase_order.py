from odoo import fields, models, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.depends('order_line.price_subtotal', 'order_line.taxes_id', 'order_line.fixed_discount_amount')
    def _amount_all(self):
        super(PurchaseOrder, self)._amount_all()
        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.order_line:
                print('price subtotal',line.price_subtotal)
                amount_untaxed = amount_untaxed + line.price_subtotal
                print('nt_untaxed...',amount_untaxed)
                if line.taxes_id:
                    discounted_price = line.price_unit - line.fixed_discount_amount
                    taxes = line.taxes_id.compute_all(
                        discounted_price,
                        order.currency_id,
                        line.product_qty,
                        product=line.product_id,
                        partner=order.partner_id
                    )
                    amount_tax += sum(tax['amount'] for tax in taxes['taxes'])

            order.update({
                'amount_untaxed': order.currency_id.round(amount_untaxed),
                'amount_tax': order.currency_id.round(amount_tax),
                'amount_total': order.currency_id.round(amount_untaxed + amount_tax),
            })
