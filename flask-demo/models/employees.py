from config.setting import db

class Employees(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(128), nullable=False)
    start_schedule = db.Column(db.String(128), nullable=False)
    end_schedule = db.Column(db.String(128), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'role': self.role,
            'start_schedule': self.start_schedule,
            'end_schedule': self.end_schedule,
        }
        