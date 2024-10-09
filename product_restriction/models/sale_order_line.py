from odoo import fields, models, api
from odoo .exceptions import  ValidationError

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    discount_validation = fields.Float(
        string="Discount validation",
        compute = "validate_discount"
    )
    #validate duplicate product from sale order lines
    @api.constrains('product_id')
    def _constrains_product_id(self):
        for line in  self:
            duplicate_lines = self.search([
                ('product_id', '=', self.product_id.id,
                 'order_id', '=' ,line.order_id,
                 'id', '!=', line.id,
                 )
            ])
            if duplicate_lines:
                raise ValidationError("Cannot add duplicate product on line")

    #validate discount limit of both product as well as product category
    def validate_discount(self):
        for line in self:

            product = line.product_id
            product_category = line.product_uom_category_id

            #get from configuratio settings
            product_discount_limit = self.env['ir.config_parameter'].sudo().get_param('sale.discount_limit_on_product')
            product_categ_discount_limit = self.env['ir.config_parameter'].sudo().get_param('ale.discount_limit_on_product_category')

            #check product discount limit
            if product.discount_limit_on_product and line.discount_validation > product_discount_limit:
                raise ValidationError("product exceed discount limit")


            #check category discount limit if product discount limit not exceed
            #if product_category:


