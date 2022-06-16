# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    def clear_tr_data(self):
        self.env['ir.sequence'].search([]).write({'number_next_actual':1})
        tables = ['account_partial_reconcile', 'mail_message', 'sale_order', 'purchase_order', 'sale_order_line',
                  'purchase_order_line', 'product_supplierinfo', 'account_move',
                  'account_move_line', 'stock_quant', 'stock_move_line',
                  'mrp_production', 'mrp_unbuild',
                  'hr_expense', 'hr_expense_sheet',
                  'stock_move', 'stock_picking', 'stock_valuation_layer', 'stock_scrap', 'account_payment',
                  'pos_payment', 'pos_order', 'pos_session', 'pos_loyalty_history', 'account_bank_statement']
        for table in tables:
            try:
                if table.replace('_','.') in self.env:
                    query = "delete from %s" % (table)
                    self.env.cr.execute(query)
                    model = table.replace("_", ".")
                    query = "delete from mail_followers where res_model = '%s'" % (model)
                    self.env.cr.execute(query)
            except:
                continue



