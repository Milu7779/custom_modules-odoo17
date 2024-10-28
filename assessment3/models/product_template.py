from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_bundle_product = fields.Boolean(string='is Bundle Product')
    is_product_pack = fields.Boolean(string='is Bundle Product')
    bundle_product_ids = fields.One2many(
        'bundle.product',
        'product_template_id',
        string='Bundle Product'
    )