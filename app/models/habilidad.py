from app import db

class Habilidad(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))

  def to_dic(self):
    return {
      "id": self.id,
      "name": self.name
    }