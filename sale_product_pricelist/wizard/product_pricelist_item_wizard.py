from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime

class ProductPricelistWizard(models.TransientModel):
    _name = 'product.pricelist.wizard'

    sale_order_line_id = fields.Many2one(
        'sale.order.line',
        string='sale wizard'
    )
    product_id = fields.Many2one(
        'product.product',
        string='Product'
    )
    pricelist_line_ids = fields.One2many(
        'pricelist.line',
        'pricelist_item_id',
        string='Pricelist '
    )

    @api.onchange('pricelist_line_ids')
    def _onchange_pricelist_line_ids(self):
        selected_pricelists = self.pricelist_line_ids.filtered(lambda r: r.selected)
        if len(selected_pricelists) > 1:
            for pricelist in selected_pricelists[1:]:
                pricelist.selected = False

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            pricelist_items = self.env['product.pricelist.item'].search([
                ('product_tmpl_id', '=', self.product_id.product_tmpl_id.id)
            ])
            pricelist_lines = [(0, 0, {
                'pricelist_id': item.pricelist_id.id,
                'selected': False,
            }) for item in pricelist_items]
            self.pricelist_line_ids = pricelist_lines


    @api.model
    def default_get(self, fields_list):
        res = super(ProductPricelistWizard, self).default_get(fields_list)

        sale_order_line_id = self._context.get('default_sale_order_line_id')
        product_id = self._context.get('default_product_id')
        res.update({
            'sale_order_line_id': sale_order_line_id,
            'product_id': product_id,

        })
        return res

    def action_apply_pricelist(self):
        selected_lines = self.pricelist_line_ids.filtered('selected')

        if not selected_lines:
            raise ValidationError("No price list selected. Please select a price list.")
        if len(selected_lines) > 1:
            raise ValidationError("Only one price list can be selected at a time.")

        today_date = fields.Date.today()
        today_datetime = datetime.combine(today_date, datetime.min.time())

        price_list = selected_lines.pricelist_id
        active_items = price_list.item_ids.filtered(
            lambda item: (not item.date_start or today_datetime >= datetime.combine(item.date_start.date(),
                                                                                           datetime.min.time())
                         ) and (
                                 not item.date_end or today_datetime <= datetime.combine(item.date_end.date(),
                                                                                         datetime.min.time())
                         )
        )
        if not active_items:
            raise ValidationError(
                f"The selected price list '{price_list.name}' has expired and cannot be applied"
            )
        sale_order_line = self.sale_order_line_id
        price_item = next((item for item in active_items if item.product_id.id == sale_order_line.product_id.id),None)
        if price_item:
            sale_order_line.price_unit = price_item.fixed_price
        return {'type': 'ir.actions.act_window_close'}



class PricelistLieWizard(models.TransientModel):

    _name = 'pricelist.line'

    pricelist_item_id = fields.Many2one(
        'product.pricelist.wizard',
        string='item pricelist '
    )
    pricelist_id = fields.Many2one(
        'product.pricelist',
        string='Pricelist Name'
    )
    selected = fields.Boolean(string='Is selected')









