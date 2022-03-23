{
    "name": "Sales commissions",
    "version": "14.0.1.1.7",
    "category": "Sales Management",
    "license": "AGPL-3",
    "depends": ["account", "product", "sale_management"],
    "website": "https://github.com/OCA/commission",
    "development_status": "Mature",
    "maintainers": ["pedrobaeza"],
    "data": [
        "security/ir.model.access.csv",
        "security/sale_commission_security.xml",
        "views/sale_commission_view.xml",
        "views/sale_commission_mixin_views.xml",
        "views/product_template_view.xml",
        "views/res_partner_view.xml",
        "views/sale_order_view.xml",
        "views/account_move_views.xml",
        "views/sale_commission_settlement_view.xml",
        "views/sale_commission_settlement_report.xml",
        "views/report_settlement_templates.xml",
        "report/sale_commission_analysis_report_view.xml",
        "wizard/wizard_settle.xml",
        "wizard/wizard_invoice.xml",
        "data/sale_agent.xml"
    ],

    "installable": True,
}
