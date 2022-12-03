from odoo import api, fields, models, _
import datetime
from odoo.exceptions import ValidationError


class SurplusCharge(models.Model):
    _name = "surplus.charge"
    _description = (
        "This Model will include details related to product's Surplus Charges"
    )
    _rec_name = "display_name"

    product_id = fields.Many2one(
        string="Product",
        comodel_name="product.product",
        domain="['&',('detailed_type','=','service'),('is_surplus_charges','=',True)]",copy=False
    )
    surplus_charges = fields.Float(string="Surplus Charge", required=True,copy=False)
    start_date = fields.Date(string="Start Date", required=True,copy=False)
    end_date = fields.Date(string="End Date", required=True,copy=False)
    active = fields.Boolean(string="Active", default=True)
    display_name = fields.Char(
        string="Display Name", default=lambda self: _("New"), compute="diplay_name"
    )

    # THIS FUNcTION WILL CHECK DATE VALIATIONS
    @api.constrains("start_date", "end_date")
    def check_date(self):
        if (
                self.start_date < datetime.date.today()
                or self.end_date < datetime.date.today()
        ):
            raise ValidationError("You Cannot Enter the Date smaller than current Date")
        if self.start_date > self.end_date:
            raise ValidationError("Start Date Must be Smaller Than End Date")

    # THIS FUNCTION WILL INITALIZE THE DISPLAY NAME
    def diplay_name(self):
        for record in self:
            record.display_name = (
                    str(record.product_id.name) + "-(" + str(record.surplus_charges) + "%)"
            )

    # THIS IS THE FUNCTION FOR CRON JOB
    def cron_check_charge_validity(self):
        charges_records = self.env["surplus.charge"].search([])
        for record in charges_records:
            if record.end_date < datetime.date.today():
                record.active = False
