from odoo import api, fields, models


class Users(models.Model):
    _inherit = "res.users"

    password_reset_url = fields.Char(related="signup_url", string="Password Reset URL")
    referral_code = fields.Char(string="Referral Code")
    city = fields.Char()
    idnumber = fields.Char()
    toc = fields.Char()
    idtype = fields.Char()
    registration_stage = fields.Selection(
        selection=[("not_verified", "Not Verified"), ("verified", "Verify")],
        string="Registration Stage",
        default="not_verified",
    )


class ResPartner(models.Model):
    _inherit = "res.partner"

    common_product_ids = fields.Many2many(comodel_name="product.product")
    contact_person = fields.Char(string="Contact Person")
    business_category = fields.Char(string="Business Category")
    number_of_offices = fields.Char(string="Number of Offices")
    referral_code = fields.Char(
        string="Referral Code", related="user_id.referral_code", store=True
    )
    city = fields.Char(related="user_id.city")
    idnumber = fields.Char(related="user_id.idnumber", store=True)
    toc = fields.Char(related="user_id.toc", store=True)
    idtype = fields.Char(related="user_id.idtype", store=True)
    business_type = fields.Char()
    purchase_frequency = fields.Float()


class ProductTemplate(models.Model):
    _inherit = "product.template"

    aisiki_product_type = fields.Selection(
        selection=[("fresh", "Fresh Food"), ("fmcg", "FMCG")], string="Aisiki Type"
    )

    image_url = fields.Char(string="Image URL", compute="_compute_image_url_link")

    def _compute_image_url_link(self):
        base_url = self.env["ir.config_parameter"].sudo().get_param("web.base.url")

        for rec in self:
            rec.image_url = "%s/web/image/%s/%s/image_1024" % (
                base_url,
                rec._name,
                rec.id,
            )


# class SaleOrder(models.Model):
#     _inherit = "sale.order"

#     @api.model
#     def create(self, values):
#         res = super(SaleOrder, self).create(values)
#         print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', self.env.context)
#         [o.write({'team_id':    sales_team.salesteam_website_sales}) for o in res]
#         return res
