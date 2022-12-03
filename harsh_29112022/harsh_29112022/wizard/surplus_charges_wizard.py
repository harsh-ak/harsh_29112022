from odoo import api, fields, models
import datetime
from odoo.exceptions import ValidationError


class SurplusChargeWizard(models.TransientModel):
    _name = "surplus.charge.wizard"
    _description = "This Wizard Will Allow you to select the surplus charge product and also update its charge"

    product_id = fields.Many2one(string="Product", comodel_name="surplus.charge")

    # THIS FUCNTION ADDS THE SELECTED SURPLUS CHARGE PRODUCT INTO SALE ORDER LINE
    def add_charges(self):
        current_sale_order_object = self.env["sale.order"].browse(
            self.env.context.get("sale_order_id")
        )
        for line in current_sale_order_object.order_line:
            if line.product_id == self.product_id.product_id:
                raise ValidationError("Cannot add the same Product Again")
            if line.product_id.is_surplus_charges == True:
                line.unlink()

        insert_product = [
            (
                0,
                0,
                {
                    "product_id": self.product_id.product_id.id,
                    "product_uom_qty": 0,
                    "price_unit": 1,
                },
            )
        ]
        current_sale_order_object.write({"order_line": insert_product})
        for line in current_sale_order_object.order_line:
            line.price_unit += (
                                           line.price_unit * self.product_id.surplus_charges
                                   ) / 100
