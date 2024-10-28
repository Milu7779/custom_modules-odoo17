from odoo import fields, models

class BundleProduct(models.Model):
    _name = "bundle.product"

    product_template_id = fields.Many2one(
        'product.template',
        'bundle_product_ids'

    )
    bundle_product_lines = fields.One2many(
        'bundle.product.line',
        'bundle_id',
        strring='bundle product lines'
    )

class BundleProductLine(models.Model):
    _name = "bundle.product.line"

    bundle_id = fields.Many2one(
        'bundle.product',
        'bundle_product_lines'

    )
    product_name = fields.Many2one('product.product',string='product')
    qty = fields.Integer(string='quantity')