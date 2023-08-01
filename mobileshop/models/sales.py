

from odoo import models, fields, api, _


class MobileSales(models.Model):
    _name = 'sale.sale'
    _rec_name = 'sale_seq'

    cname = fields.Char(string='Customer Name', required=True)
    add = fields.Char(string='Address')
    phone = fields.Char(string='Phone', required=True)
    pname = fields.Char(string='Product Name', required=True)
    imi = fields.Char(string='IMEI')
    qty = fields.Integer(string='Quantity')
    pmodel = fields.Char(string='Model')
    price = fields.Float(string='Price', required=True)
    pdate = fields.Date(string='Purchase Date')
    war = fields.Date(string='Warranty expire Date', required=True)
    man = fields.Char(string='Sales Man')

    sale_seq = fields.Char(string='Order Reference', required=True,
                          copy=False, readonly=True, index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('sale_seq', _('New')) == _('New'):
            vals['sale_seq'] = self.env['ir.sequence'].next_by_code('sale.sale.seq') or _('New')
        result = super(MobileSales, self).create(vals)
        return result

