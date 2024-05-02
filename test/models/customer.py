from odoo import models,fields,api
from datetime import datetime, date
from odoo.exceptions import ValidationError

class Customer(models.Model):
    _name = 'customer'
    _description = 'Customer'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # this is field to do sequence for property, should this field ref before name
    ref = fields.Char(default="New", readonly=1)
    name = fields.Char(required=True, size=50, default="New", tracking=1)
    phone = fields.Char('Phone', tracking=1)
    address = fields.Char('Address', tracking=1)
    active = fields.Boolean(default='true',string='active')
    lawyer_ids = fields.One2many('lawyer','customer_id', ondelete='cascade')


    @api.model
    def create(self, vals):
        rec = super(Customer, self).create(vals)
        if rec.ref == 'New':
            rec.ref = self.env['ir.sequence'].next_by_code('customer_seq')
        return rec
