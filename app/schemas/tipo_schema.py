from marshmallow import Schema, fields

class TipoSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
