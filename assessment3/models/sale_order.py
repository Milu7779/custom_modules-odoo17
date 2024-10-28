from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    pack_product_ids = fields.One2many(
        'pack.product',
        'order_id',
        string='pack products'
    )

    def action_confirm(self):

        super(SaleOrder, self).action_confirm()
        for order in self.order_line:
            for line in order.order_id:
                if line.product_id.is_bundle_product == True:
                    self.pack_products_ids = self.order_lines
                    self.picking_ids = self.order_lines



