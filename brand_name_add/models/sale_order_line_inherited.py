from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    _rec_name = 'brand_id'

    brand_id = fields.Many2one('product.brand', string='Brand', related='product_id.brand_id')
    serial_no_id = fields.Many2one('stock.lot', string = 'Serial Number')
    serial_no_ids = fields.Many2many('stock.lot', string = 'Serial Numbers')

