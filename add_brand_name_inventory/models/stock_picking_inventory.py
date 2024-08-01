from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    stock_reference = fields.Char(string='Stock Reference')


class StockMoveLines(models.Model):
    _inherit = 'stock.move'


    product_brand_id = fields.Many2one(
        'product.brand',
        string='Product Brand',
        compute='_compute_product_brand',

    )

    @api.depends('product_id')
    def _compute_product_brand(self):
        for move in self:
            if move.product_id:
                move.product_brand_id = move.product_id.product_brand_id
            else:
                move.product_brand_id = False

