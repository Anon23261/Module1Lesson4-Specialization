from app.extensions import db
from datetime import datetime

class Service(db.Model):
    __tablename__ = 'service'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    duration_hours = db.Column(db.Float)
    mechanic_id = db.Column(db.Integer, db.ForeignKey('mechanic.id', name='fk_service_mechanic_id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    __table_args__ = (
        db.Index('idx_service_mechanic_id', 'mechanic_id'),
        db.Index('idx_service_price', 'price'),
    )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'duration_hours': self.duration_hours,
            'mechanic_id': self.mechanic_id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
