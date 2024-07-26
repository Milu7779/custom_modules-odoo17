
from odoo import models,fields,api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    order_line = fields.One2many('sale.order.line','order_id',string='Order Lines')

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_brand = fields.Char(string="product Brand", related='product_id.product_brand_id.brand_name')

    on_product_brand = fields.Char(string='Product Brand Onchange')

    @api.onchange('product_id')
    def onchange_product_id(self):
        if self.product_id:
            self.on_product_brand = self.product_id.product_brand_id.brand_name
