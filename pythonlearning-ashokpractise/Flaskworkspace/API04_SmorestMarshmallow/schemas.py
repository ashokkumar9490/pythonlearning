from marshmallow import Schema, fields

class ItemSchema(Schema):
    # for dump_only, we can't pass id in request - it is for response
    id = fields.Str(dump_only=True)
    # for required, we must pass in request
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()

class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)