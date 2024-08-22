from odoo import fields, models, api

class AddProductLines(models.TransientModel):
    _name = 'product.select.wizard'

    product_id = fields.Many2many('product.product', string='Product', required=True)
    sale_wizard_id = fields.Many2one('sale.order', string='sale wizard')
    line_ids = fields.One2many('sale.order.line.wizard.line', 'wizard_id', string='Order Lines')

    @api.onchange('product_id')
    def _onchange_product_id(self):
        line_values = [(0, 0, {
            'product_id': product.id,
            'product_uom_qty': 1,
            'price_unit': product.lst_price,
        }) for product in self.product_id]
        self.line_ids = line_values
        print('ochage......', line_values)


    def add_products(self):
        sale_order = self.sale_wizard_id
        for product in self.product_id:
            self.env['sale.order.line'].create({
                'order_id': sale_order.id,
                'product_id': product.id,
                'product_uom_qty': 1,
                'price_unit': product.lst_price,
            })
        return {'type': 'ir.actions.act_window_close'}

class SaleOrderLineWizardLine(models.TransientModel):
    _name = 'sale.order.line.wizard.line'
    _description = 'Sale Order Line Wizard Line'

    wizard_id = fields.Many2one('product.select.wizard', string='Wizard Reference')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    product_uom_qty = fields.Float(string='Quantity', default=1.0)
    price_unit = fields.Float(string='Unit Price')
