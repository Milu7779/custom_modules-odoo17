
from odoo import models,fields,api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    order_line = fields.One2many('sale.order.line','order_id',string='Order Lines')

    def _action_confirm(self):
        res = super(SaleOrder, self)._action_confirm()

        for order in self:
            for line in order.order_line:
                for move in line.move_ids:
                    move.brand_name = line.product_brand

        return res


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_brand = fields.Char(string="product Brand", related='product_id.product_brand_id.brand_name')

    on_product_brand = fields.Char(string='Product Brand Onchange')

    @api.onchange('product_id')
    def onchange_product_id(self):
        if self.product_id:
            self.on_product_brand = self.product_id.product_brand_id.brand_name


class StockMove(models.Model):
    _inherit = 'stock.move'

    brand_name = fields.Char(string="Brand Name")

    @api.onchange('product_id')
    def onchange_product_id(self):
        if self.product_id:
            self.brand_name = self.product_id.product_brand_id.brand_name

