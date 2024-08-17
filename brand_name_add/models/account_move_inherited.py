from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    order_line = fields.One2many(comodel_name='sale.suggested.line', inverse_name='account_suggested_product_id', string='Suggested Product Lines')
    account_sugested_line = fields.One2many(comodel_name='account.suggested.line', inverse_name='suggest_line_ids', string='Suggested Product Lines')


