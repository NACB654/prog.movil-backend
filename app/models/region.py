from app import db

class Region(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  imagen_url = db.Column(db.String(100))
  ruta = db.relationship("Ruta", backref="region", lazy=True)

  def to_dic(self):
    return {
      "id": self.id,
      "name": self.name,
      "imagen_url": self.imagen_url
    }