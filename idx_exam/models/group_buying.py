from email.policy import default

from odoo import api, fields, models,_
from odoo.exceptions import UserError


class GroupBuying(models.Model):
    _name = "group.buying"
    _description = "團購表單"

    name = fields.Char(string='開團單號', required=True, default=lambda self: _('New'), readonly=True)
    user_id = fields.Many2one('res.users',
                              string='開團人員',
                              default=lambda self: self.env.user)
    open_date = fields.Date(string='開團日期', required=True, tracking=True)
    close_date = fields.Date(string='結單日期', required=True)
    group_buying_ids = fields.One2many('group.buying.line', 'group_buying_id', string='團購表單明細')
    active = fields.Boolean(sting='有效', default=True)

    @api.constrains('open_date', 'close_date')
    def check_date(self):
        for rec in self:
            if rec.open_date >= rec.close_date:
                raise UserError(_('開團日期需早於結單日期!'))

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('group.buying.sequence') or _('New')

        result = super(GroupBuying, self).create(vals)
        return result


class GroupBuyingLine(models.Model):
    _name = 'group.buying.line'
    _description = '團購表單明細'

    group_buying_id = fields.Many2one('group.buying', string='開團單號', required=True, ondelete='cascade')
    partner_id = fields.Many2one('res.partner', string='跟團人員', )
    product_id = fields.Many2one('product.product', string='商品')
    qty = fields.Integer(string='數量', default=1)


