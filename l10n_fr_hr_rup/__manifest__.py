# Copyright (C) 2016 Akretion (http://www.akretion.com/)

{
    "name": "Rapport RUP",
    "version": "12.0.1.0.0",
    "category": "French Localization",
    "summary": """ French fields and report for Registre Unique du Personnel """,
    "depends": ["hr_contract"],
    "data": [
        "data/report_paperformat.xml",
        "report/actions.xml",
        "report/report_rup.xml",
        "views/views.xml",
        "security/ir.model.access.csv",
    ],
    "demo": ["demo/demo.xml"],
    "auto_install": False,
    "installable": True,
    "author": u"Akretion, Odoo Community Association (OCA)",
    "license": "AGPL-3",
}