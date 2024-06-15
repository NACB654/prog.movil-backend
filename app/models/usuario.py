from app import db
from .associations import usuario_pokemon

class Usuario(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  last_name = db.Column(db.String(50))
  nickname = db.Column(db.String(80), nullable=False)
  email = db.Column(db.String(80), nullable=False)
  password = db.Column(db.String(120), nullable=False)
  imagen_url = db.Column(db.String(100))
  pokemons = db.relationship('Pokemon', secondary=usuario_pokemon, lazy='subquery',
        backref=db.backref('usuarios', lazy=True))

  def to_dic(self):
    return {
      "id": self.id,
      "name": self.name,
      "last_name": self.last_name,
      "nickname": self.nickname,
      "email": self.email,
      "password": self.password,
      "imagen_url": self.imagen_url,
      'pokemons': [pokemon.to_dict() for pokemon in self.pokemons]
    }