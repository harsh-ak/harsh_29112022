from odoo import fields, models


class Product(models.Model):
    _inherit = "product.template"

    is_surplus_charges = fields.Boolean(string="Is Surplus Charges")
