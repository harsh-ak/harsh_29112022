from odoo import fields, models, _


class SaleOrderLine(models.Model):
    _inherit = "sale.order"

    def open_wizard(self):
        return {
            "name": _("Surplus Charges Record"),
            "type": "ir.actions.act_window",
            "view_type": "form",
            "view_mode": "form",
            "res_model": "surplus.charge.wizard",
            "target": "new",
            "context": {"sale_order_id": self.id},
        }
