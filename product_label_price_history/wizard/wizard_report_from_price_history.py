# -*- coding: utf-8 -*-
# License, author and contributors information in:
# __openerp__.py file at the root folder of this module.

from openerp import models, fields, exceptions, _


class WizProductLabelFromPriceHistory(models.TransientModel):
    _inherit = 'wiz.product.label'

    date_from = fields.Datetime(
        'Date From',
        default=fields.Datetime.now(),
        required=True
    )
    quantity = fields.Selection(
        selection=[
            ('one', 'One label for each product'),
            ('total', 'Total product stock quantity'),
        ],
        string='Quantity',
        default='one',
        translate=True
    )

    def button_print_from_price_history(self, cr, uid, ids, context=None):
        wiz = self.browse(cr, uid, ids[0], context=context)
        price_history_ids = self.pool['product.price.history'].search(
            cr, uid, [('datetime', '>=', wiz.date_from)])
        price_historys = self.pool['product.price.history'].browse(
            cr, uid, price_history_ids)

        product_ids = []
        if wiz.quantity == 'one':
            product_tmpl_ids = [ph.product_template_id.id for ph in
                                price_historys]
            product_ids = self.pool['product.product'].search(
                cr, uid, [('product_tmpl_id', 'in', product_tmpl_ids)])
            product_ids = list(set(product_ids))

        elif wiz.quantity == 'total':
            products = []

            for ph in price_historys:
                product_ids = self.pool['product.product'].search(
                    cr, uid, [
                        ('product_tmpl_id', '=', ph.product_template_id.id)
                    ])

                if product_ids and product_ids[0] not in products:
                    product_ids *= int(ph.product_template_id.qty_available)
                    products = products + product_ids
            product_ids = products

        product_ids = filter(lambda x: x, product_ids)
        if not product_ids:
            raise exceptions.Warning(_('No labels for print'))
        else:
            return {
                'type': 'ir.actions.report.xml',
                'report_name': wiz.report_id.report_name,
                'datas': {'ids': product_ids},
            }
