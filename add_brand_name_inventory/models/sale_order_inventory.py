# -*- coding: utf-8 -*-

from odoo import models, fields


class SaleOrderTemplate(models.Model):
    _inherit = 'sale.order'

    stock_reference = fields.Char(string='Stock Reference')

    def _action_confirm(self):
        result = super(SaleOrderTemplate, self)._action_confirm()
        for picking in self.picking_ids:
            picking.stock_reference = self.stock_reference
            for move in picking.move_ids:  # Corrected from move_lines to move_ids
                move.stock_reference = self.stock_reference
        return result
