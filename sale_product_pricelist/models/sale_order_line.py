from odoo import fields, models, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def select_pricelist(self):
        print('clicked...')
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'price List',
            'res_model': 'product.pricelist.wizard',
            'view_mode': 'form',
            'context': {
                'default_sale_order_line_id': self.id,
                'default_product_id': self.product_id.id,
            },
            'target': 'new',
        }

