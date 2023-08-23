from app import db

class Brand(db.Model):
    __tablename__ = 'brands'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brandname = db.Column(db.String(50), unique=True)