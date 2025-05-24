from app import db
from datetime import datetime

class DataPenerima(db.Model):
    __tablename__ = 'data_penerima'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), unique=True, nullable=False)
    k1 = db.Column(db.Integer, nullable=False)
    k2 = db.Column(db.Integer, nullable=False)
    k3 = db.Column(db.Integer, nullable=False)
    k4 = db.Column(db.Integer, nullable=False)
    k5 = db.Column(db.Integer, nullable=False)
    k6 = db.Column(db.Integer, nullable=False)
    k7 = db.Column(db.Integer, nullable=False)
    cluster = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    
    def __repr__(self):
        return f'<DataPenerima {self.nama}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'nama': self.nama,
            'k1': self.k1,
            'k2': self.k2,
            'k3': self.k3,
            'k4': self.k4,
            'k5': self.k5,
            'k6': self.k6,
            'k7': self.k7,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }