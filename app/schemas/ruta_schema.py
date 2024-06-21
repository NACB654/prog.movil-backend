from marshmallow import Schema, fields

class RutaSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    imagen_url = fields.Url(require_tld=False)
    region_id = fields.Int(required=True)
    pokemones = fields.List(fields.Nested('PokemonSchema'))
