from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    brand_id = fields.Many2one('product.brand', string='Brand')


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    stock_reference = fields.Char(string='Stock Reference')

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
        res1 = super(SaleOrder, self)._create_invoices(self)

        sale_order_lines = self.mapped('order_line')

        for line in sale_order_lines:
            account_moves = self.env['account.move.line'].search([('sale_line_ids', 'in', line.id)])
            for acc_move in account_moves:
                acc_move.serial_no_id = line.serial_no_id
                acc_move.brand_id = line.brand_id

        return res1

