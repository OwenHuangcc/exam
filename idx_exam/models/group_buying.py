from odoo import api, fields, models
from pkg_resources import require


class GroupBuying(models.Model):
    _name = "group.buying"
    _description ="團購表單"

    name = fields.Char(string='開團單號', required=True)
    user_id = fields.Many2one(string='開團人員', readonly=False)
    open_date = fields.Date(string='開團日期', readonly=False, required=True, tracking=True)
    close_date = fields.Date(string='結單日期', readonly=False, required=True)
    group_buying_ids = fields.One2many('group.buying.line','group_buying_id')
    active = fields.Boolean(sting='有效', readonly=False)


class GroupBuyingLine(models.Model):
    _name ='group.buying.line'
    _description = '團購表單明細'

    group_buying_id = fields.Many2one('group.buying',string='開團單號', required=True, ondelete='cascade')
    partner_id = fields.Many2one('res.partner', string='跟團人員', readonly=False )
    product_id = fields.Many2one('product.product', string='商品', readonly=False)
    qty = fields.Integer(string='數量', readonly=False, default= 1)


