from marshmallow import Schema, fields

class RegionSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    descripcion = fields.Str(required=False)
    imagen_url = fields.Url(require_tld=False)
    rutas = fields.List(fields.Nested('RutaSchema'))
