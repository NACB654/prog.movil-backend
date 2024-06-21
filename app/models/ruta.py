from app import db

class Ruta(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  region_id = db.Column(db.Integer, db.ForeignKey("region.id"), nullable=False)

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'region_id': self.region_id
    }