# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "harsh_29112022",
    "version": "1.0",
    "summary": "Surplus Charges",
    "sequence": 10,
    "description": """
This Module will able to allow the sales manager to add the surplus charges while creating an Quotation
    """,
    "depends": ["sale_management"],
    "data": [
        "security/ir.model.access.csv",
        "data/cron_check_active_charges.xml",
        "views/product_inherit.xml",
        "views/surplus_charges_view.xml",
        "views/sale_view_inherit.xml",
        "wizard/surplus_charges_wizard_views.xml",
    ],
    "demo": [],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
