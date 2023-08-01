# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class mobileshop(models.Model):
    _name = 'mob.mob'
    _description = 'mobileshop.mobileshop'

    name = fields.Char(string='Name', required=True)
    imei = fields.Integer(string='IMEI', required=True)
    model = fields.Char(string='Model',required=True)
    qty = fields.Integer(string='Quantity')
    sd = fields.Date(string='Stock Date')
    cp = fields.Float(string='Company Price', required=True)
    csp = fields.Float(string='Customer Price')

    mob_seq = fields.Char(string='Order Reference', required=True,
                           copy=False, readonly=True, index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('mob_seq', _('New')) == _('New'):
            vals['mob_seq'] = self.env['ir.sequence'].next_by_code('mob.mob.seq') or _('New')
        result = super(mobileshop, self).create(vals)
        return result


