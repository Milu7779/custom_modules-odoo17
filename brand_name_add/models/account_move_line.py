from odoo import models, fields

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    brand_id = fields.Many2one('product.brand', string='Brand')
    serial_no_id = fields.Many2one('stock.lot', string='Serial_number')