from config.setting import db

class Enclosures(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    location = db.Column(db.String(128), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
        }
        