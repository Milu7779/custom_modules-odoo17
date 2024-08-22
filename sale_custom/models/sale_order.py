from odoo import fields, models, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order'



    def add_product_wizard_action(self):
        print('clicked...')

        return {
            'type': 'ir.actions.act_window',
            'name': 'Add Products',
            'res_model': 'product.select.wizard',
            'view_mode': 'form',
            'context': {
                'default_sale_wizard_id': self.id,
            },
            'target': 'new',
        }

