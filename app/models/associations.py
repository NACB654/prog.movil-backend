from app import db

usuario_pokemon = db.Table('usuario_pokemon',
    db.Column('usuario_id', db.Integer, db.ForeignKey('usuario.id'), primary_key=True),
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id'), primary_key=True)
)