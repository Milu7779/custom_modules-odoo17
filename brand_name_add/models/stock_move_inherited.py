from odoo import models, fields

class StockMove(models.Model):
    _inherit = 'stock.move'

    brand_id = fields.Many2one('product.brand', string='Brand')
    stock_reference = fields.Char(string='Stock Reference')
    serial_no_id = fields.Many2one('stock.lot', string='Serial number')
    serial_no_ids = fields.Many2many('stock.lot', string='Serial numbers')

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    stock_reference = fields.Char(string='Stock Reference')

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    serial_no_id = fields.Many2one('stock.lot', string='Serial number')
    serial_no_ids = fields.Many2many('stock.lot', string='Serial numbers')