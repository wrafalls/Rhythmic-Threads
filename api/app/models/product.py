from apiflask import Schema, fields
from datetime import datetime


class Product(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    description = fields.String(required=True)
    collection = fields.String(required=True)
    category = fields.String(required=True)
    sx = fields.String(required=True)
    size = fields.String(required=True)
    price = fields.Float(required=True)
    ratings = fields.Integer(allow_none=True)
    created = fields.DateTime(dump_only=True, dump_default=datetime.now())
    updated = fields.DateTime(dump_only=True, dump_default=datetime.now())


class ProductRequest(Schema):
    name = fields.String()
    description = fields.String()
    collection = fields.String()
    category = fields.String()
    sx = fields.String()
    size = fields.String()
    price = fields.Float()
    ratings = fields.Integer(allow_none=True)
    created = fields.DateTime(dump_default=datetime.now())
    updated = fields.DateTime(allow_none=True)


class ProductResponse(Schema):
    id = fields.Integer()
    name = fields.String()
    description = fields.String()
    collection = fields.String()
    category = fields.String()
    sx = fields.String()
    size = fields.String()
    price = fields.Float()
    ratings = fields.Integer(allow_none=True)
    created = fields.DateTime()