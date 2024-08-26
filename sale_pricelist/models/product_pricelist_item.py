from odoo import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)

class ProductPricelistItem(models.Model):
    _inherit = 'product.pricelist.item'


    compute_price = fields.Selection(selection_add=[('tiered', 'Tiered')],ondelete={'tiered': 'set default'})
    Tier_lines = fields.One2many(comodel_name='product.tier.line', inverse_name='tier_id', string='Tiers')
    product_variant_ids = fields.Many2one('product.product', string='product variants')





