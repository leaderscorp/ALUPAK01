# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def submit_for_approval_1(self):
        for rec in self:
            rec.state = 'waiting_for_approval_1'


    def submit_for_approval_2(self):
        for rec in self:
            rec.state = 'waiting_for_approval_2'


    def approve_sale_order(self):
        #for rec in self:
            #rec.action_confirm()
            #rec.state = 'sale'
        res = super(SaleOrder, self).action_confirm()
        return res

    # @api.multi
    # def write(self, vals):
    #     if any(state == 'waiting_for_approval_1' for state in set(self.mapped('state'))):
    #         raise UserError(_("No edit in done state"))
    #     else:
    #         return super().write(vals)
    
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('waiting_for_approval_1', 'Waiting For First Approval'),
        ('waiting_for_approval_2', 'Waiting For Second Approval'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')