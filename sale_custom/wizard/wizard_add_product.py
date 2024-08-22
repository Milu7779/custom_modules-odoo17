from odoo import fields, models, api

class AddProductLines(models.TransientModel):
    _name = 'product.select.wizard'

    product_id = fields.Many2many('product.product', string='Product', required=True)
    sale_wizard_id = fields.Many2one('sale.order', string='sale wizard')

    def add_products(self):
        sale_order = self.sale_wizard_id
        for product in self.product_id:
            self.env['sale.order.line'].create({
                'order_id': sale_order.id,
                'product_id': product.id,
                'product_uom_qty': 1,
            })
        return {'type': 'ir.actions.act_window_close'}
