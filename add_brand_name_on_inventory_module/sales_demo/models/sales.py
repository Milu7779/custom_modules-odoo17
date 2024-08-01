from odoo import models,fields



class SaleOrder(models.Model):
    _inherit = 'sale.order'

    cust_location = fields.Char(string="Customer Location")
    #order_line = fields.One2many('sale.order.line','order_id',string='Order Lines')
    #product_brand = fields.Char(string="product Brand",related='name.product_brand')
    #def test_button_function(self):
        #print('test btn clicked...')






