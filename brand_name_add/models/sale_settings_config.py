from odoo import fields, models, api

class SaleSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    last_no_of_orders = fields.Integer('No of orders', config_parameter='sale.last_no_of_orders')
    last_no_of_days_orders = fields.Integer('Last no of days orders', config_parameter='sale.last_no_of_days_orders')
    enable_recorder = fields.Boolean('Enable Reorder', default=False, config_parameter='sale.enable_recorder')
    order_stages = fields.Selection(
        [('all', 'All'),
         ('draft', 'Draft'),
         ('sent', 'Sent'),
         ('sale', 'Sale'),
         ('done', 'Done'),
         ('cancel', 'Cancelled')],
        config_parameter='sale.order_stages',
        string="Order Stages",
        help="Stages of the orders",
        default='all'
    )
    sale_settings_id = fields.Many2one(
        comodel_name='sale.order',
        inverse_name='sale_settings_id',
        string='Order history setting'
    )

