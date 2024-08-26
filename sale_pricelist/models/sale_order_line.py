from odoo import models, api


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"



    @api.onchange('product_uom_qty', 'product_id', 'order_id')
    def _onchange_product_uom_qty(self):
        for line in self:
            if line.product_id and line.product_uom_qty and line.order_id:
                pricelist = line.order_id.pricelist_id

                # Filter the pricelist items for the selected product and tiered pricing
                pricelist_item = pricelist.item_ids.filtered(
                    lambda item: item.product_variant_ids == line.product_id and item.compute_price == 'tiered'
                )
                if pricelist_item:
                    tiered_price = self._get_tiered_price(pricelist_item, line.product_uom_qty)
                    line.price_unit = tiered_price if tiered_price else line.product_id.lst_price
                else:
                    line.price_unit = line.product_id.lst_price

    def _get_tiered_price(self, pricelist_item, quantity):
        # Loop through tiered prices to find the appropriate price based on quantity
        for tier in pricelist_item.Tier_lines:
            if tier.tire_from <= quantity <= tier.tire_to:
                return tier.list_price
        return 0.0