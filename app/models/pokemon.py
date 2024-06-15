from app import db

class Pokemon(db.model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  index = db.Column(db.Integer)
  weight = db.Column(db.Integer)
  height = db.Column(db.Integer)
  description = db.Column(db.String(200))
  attack = db.Column(db.Integer)
  defense = db.Column(db.Integer)
  sp_attack = db.Column(db.Integer)
  sp_defense = db.Column(db.Integer)
  speed = db.Column(db.Integer)
  audio_url = db.Column(db.String(100))
  sprite_url = db.Column(db.String(100))
  imagen_url = db.Column(db.String(100))

  def to_dic(self):
    return {
      "name": self.id,
      "index": self.index,
      "weight": self.weight,
      "height": self.height,
      "description": self.description,
      "attack": self.attack,
      "defense": self.defense,
      "sp_attack": self.sp_attack,
      "sp_defense": self.sp_defense,
      "speed": self.speed,
      "audio_url": self.audio_url,
      "sprite_url": self.sprite_url,
      "imagen_url": self.imagen_url
    }