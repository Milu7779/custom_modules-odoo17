from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    stock_reference = fields.Char(string = 'Stock Reference')

    @api.model
    def create(self, vals):
        order = super(SaleOrder, self).create(vals)
        for picking in order.picking_ids:
            picking.stock_reference = order.stock_reference
        return order

    def _action_confirm(self):
        result = super(SaleOrder, self)._action_confirm()
        for pickings in self.picking_ids:
            pickings.stock_reference = self.stock_reference
        return result


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    stock_reference = fields.Char(string='Stock Reference')