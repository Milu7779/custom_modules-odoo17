from odoo import models, fields

class ProductTierLine(models.Model):
    _name = 'product.tier.line'

    tier_id = fields.Many2one(comodel_name='product.pricelist.item',ondelete='cascade')
    tier_no = fields.Integer(string="Tire ID")
    tire_from = fields.Float(string='Tire From')
    tire_to = fields.Float(string='Tire To')
    list_price = fields.Float(string='List Price')
