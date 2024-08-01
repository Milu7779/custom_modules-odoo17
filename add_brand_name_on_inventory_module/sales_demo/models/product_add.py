from odoo import fields, models, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_brand_id = fields.Many2one('product.brand',string="Product Brand")

    @api.onchange(product_brand_id)
    def onchange_product_brand_id(self):
       if self.product_brand_id:
            self.brand_name = f"{self.product_brand_id.brand_name}"
