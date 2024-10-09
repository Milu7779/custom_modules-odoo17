from odoo import fields, models, api
from odoo .exceptions import  ValidationError

class PurchaseOrderLine(models.Model):

    _inherit = 'purchase.order.line'

    @api.constrains('product_id')
    def _constrains_product_id(self):
        for line in  self:
            duplicate_lines = self.search([
                ('product_id' ,'=', self.product_id.id,
                 'order_id', '=' ,line.order_id,
                 'id', '!=', line.id,
                 )
            ])
            if duplicate_lines:
                raise ValidationError("Cannot add duplicate product on line")
