from odoo import fields, models, api

class PackProduct(models.Model):
    _name = "pack.product"

    order_id = fields.Many2one('sale.order','pack_product_ids')
    calculate_pack_price = fields.Boolean(string='calculate pack price')
    sales_price = fields.Float(string='sales_price')

    @api.onchange('calculate_pack_price')
    def _onchange_calculate_pack_price(self):
        final_qty = 0
        if self.calculate_pack_price == True:
            for order in  self.order_id:
                for line in order.order_id:
                    bundle_products = line.product_id.mapped('bundle_product_ids')
                    sum=0

                    for product in bundle_products.qty:
                        sum_qty = sum + product.qty
                        final_qty=sum_qty
            self.sales_price = final_qty


