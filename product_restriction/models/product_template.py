from odoo import fields, models, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    discount_limit_on_product = fields.Float(
        string="Discount (%) Limit of product"
    )