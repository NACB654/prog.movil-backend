from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=False)
    last_name = fields.Str(required=False)
    nickname = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    imagen_url = fields.Url(require_tld=False)
