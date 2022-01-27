from marshmallow import fields
from odoo.addons.datamodel.core import Datamodel


class DatamodelErrorOut(Datamodel):
    _name = "datamodel.error.out"

    message = fields.String(required=False, allow_none=True)
    error = fields.Boolean(required=False, allow_none=True)


class OrderingAppRegisterLogin(Datamodel):
    _name = "orderingapp.login.datamodel.in"

    phone = fields.String(required=True, allow_none=False)
    password = fields.String(required=True, allow_none=False)


class OrderingAppRegisterLoginOut(Datamodel):
    _name = "orderingapp.login.datamodel.out"

    session_id = fields.String(required=True, allow_none=False)
    expires_at = fields.DateTime(required=True, allow_none=False)
    uid = fields.Integer(required=True, allow_none=False)
    username = fields.String(required=True, allow_none=False)
    name = fields.String(required=True, allow_none=False)
    partner_id = fields.Integer(required=True, allow_none=False)


class ForgotPasswordDatamodelIn(Datamodel):
    _name = "forgotpassword.datamodel.in"

    phone = fields.String(required=True, allow_none=False)


class ForgotPasswordDatamodelOut(Datamodel):
    _name = "forgotpassword.datamodel.out"

    password_reset_url = fields.String(required=False, allow_none=True)


class IndividualRegisterIn(Datamodel):
    _name = "individual.register.datamodel.in"

    name = fields.String(required=True, allow_none=False)
    phone = fields.String(required=True, allow_none=False)
    latitude = fields.Float(required=True, allow_none=False)
    longitude = fields.Float(required=True, allow_none=False)
    password = fields.String(required=True, allow_none=False)
    referral_code = fields.String(required=True, allow_none=False)
    food_items = fields.List(fields.Integer(), required=False, allow_none=False)


class IndividualRegisterOut(Datamodel):
    _name = "individual.register.datamodel.out"

    name = fields.String(required=True, allow_none=False)
    phone = fields.String(required=True, allow_none=False)
    latitude = fields.Float(required=True, allow_none=False)
    longitude = fields.Float(required=True, allow_none=False)
    referral_code = fields.String(required=True, allow_none=False)
    food_items = fields.List(fields.Integer(), required=False, allow_none=False)


class CorporateRegisterIn(Datamodel):
    _name = "corporate.register.datamodel.in"

    name = fields.String(required=True, allow_none=False)
    contact_person = fields.String(required=True, allow_none=False)
    business_category = fields.String(required=True, allow_none=False)
    password = fields.String(required=True, allow_none=False)
    number_of_offices = fields.Integer(required=True, allow_none=False)
    phone = fields.String(required=True, allow_none=False)
    latitude = fields.Float(required=True, allow_none=False)
    longitude = fields.Float(required=True, allow_none=False)
    referral_code = fields.String(required=True, allow_none=False)
    logo = fields.String(required=False, allow_none=True)
    number_of_offices = fields.Integer(required=False, allow_none=True)
    food_items = fields.List(fields.Integer(), required=False, allow_none=False)


class CorporateRegisterOut(Datamodel):
    _name = "corporate.register.datamodel.out"

    name = fields.String(required=True, allow_none=False)
    contact_person = fields.String(required=True, allow_none=False)
    phone = fields.String(required=True, allow_none=False)
    latitude = fields.Float(required=True, allow_none=False)
    longitude = fields.Float(required=True, allow_none=False)
    referral_code = fields.String(required=True, allow_none=False)
    food_items = fields.List(fields.Integer(), required=False, allow_none=False)


class Fooditems(Datamodel):
    _name = "fooditems.datamodel.out"

    id = fields.Integer(required=False, allow_none=False)
    name = fields.String(required=False, allow_none=False)
    type = fields.String(required=False, allow_none=True)
    image_url = fields.Url(required=False, allow_none=False)
    qty_available = fields.Integer(required=True, allow_none=False)
    price = fields.Decimal(required=True, allow_none=False)
    internal_ref = fields.String(required=True, allow_none=False)
    barcode = fields.String(required=True, allow_none=False)
    virtual_available = fields.Integer(required=True, allow_none=False)


class WalletBalance(Datamodel):
    _name = "wallet.balance.datamodel.out"

    balance = fields.Decimal(required=True, allow_none=False)



class CartIn(Datamodel):
    _name = "cart.datamodel.in"

    balance = fields.Decimal(required=True, allow_none=False)


class CartOut(Datamodel):
    _name = "cart.datamodel.out"

    balance = fields.Decimal(required=True, allow_none=False)
