from odoo import api, fields, models

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    @api.onchange('product_id', 'product_qty')
    def _onchange_product_id(self):
        self.price_unit = 0
        super(PurchaseOrderLine, self)._compute_price_unit_and_date_planned_and_name()

        if not self.product_id or not self.product_qty:
            return
        supplierinfo = self.env['product.supplierinfo'].search([
            ('product_tmpl_id', '=', self.product_id.product_tmpl_id.id),
            ('partner_id', '=', self.order_id.partner_id.id)
        ], limit=1)

        if supplierinfo:
            applicable_tiers = self.env['product.tier.line'].search([
                ('pricelist_item_id', '=', supplierinfo.id),
            ], order='tier_from ASC')

            if applicable_tiers:
                first_tier = applicable_tiers[0]
                if self.product_qty == first_tier.tier_to:
                    self.price_unit = first_tier.list_price
                    print('Updated Price Unit to First Tier:', self.price_unit)
                    return
                for tier in applicable_tiers[1:]:
                    if tier.tier_from <= self.product_qty <= tier.tier_to:
                        self.price_unit = tier.list_price
                        print('Updated Price Unit to Other Tier:', self.price_unit)
                        break
            else:
                print('No applicable tier found.')
        else:
            print('No supplier info found.')

