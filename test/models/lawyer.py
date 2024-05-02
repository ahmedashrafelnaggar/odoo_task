from odoo import models,fields,api
from odoo.exceptions import ValidationError
from datetime import datetime, date


class Lawyer(models.Model):
    _name = 'lawyer'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'ref'

    customer_id = fields.Many2one('customer', ondelete='cascade')
    ref = fields.Char(related='customer_id.ref', readonly=1)
    name = fields.Char(related='customer_id.name', readonly=1)
    phone = fields.Char(related='customer_id.phone', readonly=1, )
    address = fields.Char(related='customer_id.address', readonly=0)
    start_date = fields.Datetime(default=fields.Datetime.now())
    end_date = fields.Datetime()
    duration = fields.Char(string='Duration', compute="_compute_duration")
    expected_selling_price_date = fields.Date(tracking=1)
    active = fields.Boolean(default='true', string='active')

    @api.depends("start_date", "end_date")
    def _compute_duration(self):
        for record in self:
            if record.start_date and record.end_date:
                # you should make end date - start date
                delta = record.end_date - record.start_date
                record.duration = delta.days
            else:
                record.duration = 0.0

    @api.onchange('customer_id')
    def onchange_customer_id(self):
        for rec in self:
            rec.ref = rec.customer_id.ref



