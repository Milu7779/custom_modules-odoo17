from odoo import api, fields, models


class SupplierInfo(models.Model):
    _inherit = "product.supplierinfo"

    tier_ids = fields.One2many(
        comodel_name='product.tier.line',
        inverse_name='pricelist_item_id',
        string='Tiers'
    )