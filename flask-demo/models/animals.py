from config.setting import db

class Animals(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'), nullable=True)
    name = db.Column(db.String(128), nullable=False)
    species = db.Column(db.String(128), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(128), nullable=False)
    special_req = db.Column(db.String(128), default='None', nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'enclosure_id': self.enclosure_id,
            'name': self.name,
            'species': self.species,
            'age': self.age,
            'gender': self.gender,
            'special_req': self.special_req,
        }
        