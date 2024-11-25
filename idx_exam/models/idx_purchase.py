from odoo import api, fields, models

class IdxPurchase(models.Model):
    _inherit = 'purchase.order'

    is_centralized = fields.Boolean(string='團購', readonly=False)