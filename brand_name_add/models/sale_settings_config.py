from odoo import fields, models, api

class SaleSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    last_no_of_orders = fields.Integer(string='No of orders')
    last_no_of_days_orders = fields.Integer(string='Last no of days orders')
    enable_recorder = fields.Boolean(string='Enable Recorder', default=False)
    sale_settings_id = fields.Many2one(
        comodel_name='sale.order',
        inverse_name='sale_settings_id',
        string='Order history setting')


    def get_values(self):
        res = super(SaleSettings, self).get_values()
        res.update(
            last_no_of_orders=self.env['ir.config_parameter'].sudo().get_param('sale.last_no_of_orders'),
            last_no_of_days_orders=self.env['ir.config_parameter'].sudo().get_param('sale.last_no_of_days_orders'),
            #enable_recorder =  self.env['ir.config_parameter'].sudo().get_param('sale.enable_recorder', default='False') == 'True',
        )
        return res

    def set_values(self):
        super(SaleSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('sale.last_no_of_orders', self.last_no_of_orders)
        self.env['ir.config_parameter'].sudo().set_param('sale.last_no_of_days_orders', self.last_no_of_days_orders


































                                                         )
        #self.env['ir.config_parameter'].sudo().set_param('sale.enable_recorder', str(int(self.enable_recorder)))