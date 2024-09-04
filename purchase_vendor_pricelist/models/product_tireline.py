from odoo import api, fields, models


class ProductTierline(models.Model):
    _name = "product.tier.line"

    pricelist_item_id =  fields.Many2one(
        comodel_name='product.supplierinfo',
        inverse_name='tier_ids',
        string='Tier Line',
        ondelete='cascade'
    )
    tier_no = fields.Integer(string="Tire ID")
    tier_from = fields.Float(string='Tire From')
    tier_to = fields.Float(string='Tire To')
    list_price = fields.Float(string='List Price')