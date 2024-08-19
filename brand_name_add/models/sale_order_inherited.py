from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import UserError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    brand_id = fields.Many2one('product.brand', string='Brand')


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    stock_reference = fields.Char(string='Stock Reference')
    suggested_product_line = fields.One2many(
        comodel_name='sale.suggested.line',
        inverse_name='suggested_product_id',
        string='Suggested Product Lines')
    sale_order_history_id = fields.One2many(
        comodel_name='sale.order.history',
        inverse_name='sale_order_history_line_id',
        string='sale Order')
    """sale_settings_id = fields.One2many(
        comodel_name='res.config.settings',
        inverse_name='sale_settings_id',
        string='sale Order history')"""

    """@api.onchange('partner_id')
    def _onchange_partner_id(self):

        config_param = self.env['ir.config_parameter'].sudo()
        last_no_of_orders = int(config_param.get_param('sale.last_no_of_orders', default=0))
        last_no_of_days_orders = int(config_param.get_param('sale.last_no_of_days_orders', default=0))
        print('setting.....', last_no_of_orders)

        if self.partner_id:
            config_param = self.env['ir.config_parameter'].sudo()

            # Get configuration settings
            last_no_of_orders = int(config_param.get_param('sale.last_no_of_orders', default=0))
            last_no_of_days_orders = int(config_param.get_param('sale.last_no_of_days_orders', default=0))

            domain = [
                ('partner_id', '=', self.partner_id.id),
                ('state', 'in', ['sale', 'done'])
            ]
            #if self.id:
                #domain.append(('id', '!=', self.id))

            if last_no_of_days_orders > 0:
                # Filter by the last number of days
                date_from = datetime.now() - timedelta(days=last_no_of_days_orders)
                domain.append(('date_order', '>=', date_from))

            # Fetch the orders based on the domain
            previous_orders = self.env['sale.order'].search(domain, limit=last_no_of_orders, order='date_order desc')

            self.sale_order_history_id = [(6, 0, previous_orders.ids)]
        else:
            self.sale_order_history_id = [(5, 0, 0)]"""

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:

            config_param = self.env['ir.config_parameter'].sudo()
            last_no_of_orders = int(config_param.get_param('sale.last_no_of_orders', 0))
            last_no_of_days_orders = int(config_param.get_param('sale.last_no_of_days_orders', 0))
            order_state = config_param.get_param('sale.order_stages', default='all')

            date_limit = datetime.today() - timedelta(days=last_no_of_days_orders)

            domain = [
                ('partner_id', '=', self.partner_id.id),
                ('date_order', '>=', date_limit)
            ]
            if order_state != 'all':
                domain.append(('state', '=', order_state))

            previous_orders = self.env['sale.order'].search(domain, limit=last_no_of_orders)
            order_lines = []

            for prev_order in previous_orders:

                    for line in prev_order.order_line:
                        order_lines.append((0, 0, {
                                'sale_order_id': prev_order.name,
                                'order_date': prev_order.date_order,
                                'product_name': line.product_id,
                                'price': line.price_unit,
                                'qty': line.product_uom_qty,
                                'discount': line.discount,
                                'sub_total': line.price_subtotal,
                                'order_status': line.state,
                        }))
            self.sale_order_history_id = order_lines
        """if self.partner_id:
            config = self.env['res.config.settings'].search([], limit=1)
            if not config:
                raise UserError("Configuration settings are missing.")

            config_param = self.env['ir.config_parameter'].sudo()
            last_no_of_orders = int(config_param.get_param('sale.last_no_of_orders', default=0))
            last_no_of_days_orders = int(config_param.get_param('sale.last_no_of_days_orders', default=0))

            last_no_of_orders = config.last_no_of_orders
            last_no_of_days_orders = config.last_no_of_days_orders

            today = datetime.today().date()
            date_threshold = today - timedelta(days=last_no_of_days_orders)

            domain = [
                ('partner_id', '=', self.partner_id.id),
                ('date_order', '>=', date_threshold)
            ]

            order_history = self.env['sale.order'].search(domain, limit=last_no_of_orders, order='date_order desc')

            self.sale_order_history_id = [(6, 0, order_history.ids)]
        else:
            self.sale_order_history_id = [(5, 0, 0)]"""


    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()

        for picking in self.picking_ids:
            picking.stock_reference = self.stock_reference
            for move in picking.move_ids:
                move.stock_reference = self.stock_reference

        sale_order_lines = self.mapped('order_line')

        for line in sale_order_lines:

            stock_moves = self.env['stock.move'].search([('sale_line_id', '=', line.id)])
            for move in stock_moves:
                move.brand_id = line.brand_id
                move.serial_no_id = line.serial_no_id
                move.serial_no_ids = line.serial_no_ids

            stock_moves_line = self.env['stock.move.line'].search([('move_id.sale_line_id', '=', line.id)])
            for move_line  in stock_moves_line:
               move_line.serial_no_id = line.serial_no_id
               move_line.serial_no_ids = line.serial_no_ids
               move_line.lot_id = line.serial_no_id

            """account_moves = self.env['account.move.line'].search([('sale_line_ids', 'in', line.id)])
            for acc_move in account_moves:
                acc_move.brand_id = line.serial_no_id"""


        return res

    def _create_invoices(self, grouped=False, final=False):
        res1 = super(SaleOrder, self)._create_invoices(grouped,final)

        sale_order_lines = self.mapped('order_line')

        for line in sale_order_lines:
            account_moves = self.env['account.move.line'].search([('sale_line_ids', 'in', line.id)])
            for acc_move in account_moves:
                acc_move.serial_no_id = line.serial_no_id
                acc_move.brand_id = line.brand_id

        for order in self:
            for invoice in res1:
                suggested_lines = []
                for line in order.suggested_product_line:
                    suggested_lines.append((0, 0, {
                        'product_id': line.product_id.id,
                        'product_qty': line.product_qty,
                        'product_unit_price': line.product_unit_price,
                        'total_amount': line.total_amount,
                    }))
                if suggested_lines:
                    invoice.account_sugested_line = suggested_lines




        return res1

    def action_reorder(self):

        config_param = self.env['ir.config_parameter'].sudo()
        enable_reorder = config_param.get_param('sale.enable_recorder', 0)
        if enable_reorder != 'True':
            raise UserError('You do not have access to reorder because the eable_recorder parameter is not enabled.')
        else:

            order = self.env['sale.order'].create({
                'partner_id': self.partner_id.id,
            })

            order_lines = []
            for history in self.sale_order_history_id.filtered('re_order'):
                order_lines.append((0, 0, {
                    'product_id': history.product_name.id,
                    'product_uom_qty': history.qty,
                    'price_unit': history.price,
                    'discount': history.discount,
                }))

            order.write({
                'order_line': order_lines,
                'state': 'sent',
            })

            return {
                'type': 'ir.actions.act_window',
                'name': 'Sale Order',
                'view_mode': 'form',
                'res_model': 'sale.order',
                'res_id': order.id,
                'target': 'current',
            }






