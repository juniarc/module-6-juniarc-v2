from config.setting import db

class Visitors(db.Model):
    __tablename__ = 'visitors'

    id = db.Column(db.Integer, primary_key=True)
    ticket_type = db.Column(db.String(128), nullable=False)
    date = db.Column(db.String(128), nullable=False)
    event_type = db.Column(db.String(128), nullable=False)
    feedback = db.Column(db.String(128), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'ticket_type': self.ticket_type,
            'date': self.date,
            'event_type': self.event_type,
            'feedback': self.feedback,
        }
        