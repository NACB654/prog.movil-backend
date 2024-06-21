from app import db

# Asociación entre Usuarios y Pokemones
usuario_pokemon = db.Table('usuario_pokemon',
    db.Column('usuario_id', db.Integer, db.ForeignKey('usuario.id'), primary_key=True),
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id'), primary_key=True)
)

# Asociación entre Pokemones y Tipos
pokemon_tipo = db.Table('pokemon_tipo',
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id'), primary_key=True),
    db.Column('tipo_id', db.Integer, db.ForeignKey('tipo.id'), primary_key=True)
)

# Asociación entre Pokemones y Habilidades
pokemon_habilidad = db.Table('pokemon_habilidad',
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id'), primary_key=True),
    db.Column('habilidad_id', db.Integer, db.ForeignKey('habilidad.id'), primary_key=True)
)

# Asociación entre Pokemones y Rutas
pokemon_ruta = db.Table('pokemon_ruta',
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id'), primary_key=True),
    db.Column('ruta_id', db.Integer, db.ForeignKey('ruta.id'), primary_key=True)
)

amigos = db.Table('amigos',
    db.Column('usuario1_id', db.Integer, db.ForeignKey('usuario.id'), primary_key=True),
    db.Column('usuario2_id', db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
)