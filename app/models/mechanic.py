from app.extensions import db
from datetime import datetime

class Mechanic(db.Model):
    __tablename__ = 'mechanic'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100))
    email = db.Column(db.String(120), nullable=False)
    certification = db.Column(db.String(100))
    years_experience = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    services = db.relationship('Service', backref='mechanic', lazy=True)
    
    __table_args__ = (
        db.UniqueConstraint('email', name='uq_mechanic_email'),
    )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'specialty': self.specialty,
            'email': self.email,
            'certification': self.certification,
            'years_experience': self.years_experience,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
