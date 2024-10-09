from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    discount_limit_on_product = fields.Float(
        string="Discount (%) Limit of product",
        config_parameter='sale.discount_limit_on_product'
    )
    discount_limit_on_product_category = fields.Float(
        string="Discount (%) Limit of product category",
        config_parameter='sale.discount_limit_on_product_category'
    )

