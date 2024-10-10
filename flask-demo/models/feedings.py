from config.setting import db

class Feedings(db.Model):
    __tablename__ = 'feedings'

    id = db.Column(db.Integer, primary_key=True)
    animal_id = db.Column(db.Integer, db.ForeignKey('animals.id'), nullable=True)
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'), nullable=True)
    food_type = db.Column(db.String(128), nullable=False)
    feeding_time = db.Column(db.String(128), nullable=False)
    reminder = db.Column(db.String(128), nullable=False)

    animals = db.relationship('Animals', backref='feedings')
    enclosures = db.relationship('Enclosures', backref='feedings')

    def to_dict(self):
        return {
            'id': self.id,
            'animal_id': self.animal_id,
            'enclosure_id': self.enclosure_id,
            'food_type': self.food_type,
            'feeding_time': self.feeding_time,
            'reminder': self.reminder,
        }
        