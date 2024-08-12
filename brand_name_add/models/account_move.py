from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move.'

    brand_id = fields.Many2one('product.brand', string='Brand')

    """def action_post(self):
        res1 = super(AccountMove, self).action_post()

        account_move_lines = self.mapped('line_ids')
        for line in account_move_lines:
            account_moves = self.env['account.move.line'].search([('sale_line_ids', 'in', line.id)])"""