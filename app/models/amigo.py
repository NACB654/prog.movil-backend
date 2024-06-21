from app import db

class Amigo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    sprite_url = db.Column(db.String(100))
    pokemon_caught = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "sprite_url": self.sprite_url,
            "pokemon_caught": self.pokemon_caught
        }
