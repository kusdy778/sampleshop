from app import db

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(255), nullable=False)  # NOT NULL
    barcode = db.Column(db.String(50), unique=True)
    price = db.Column(db.Float, nullable=False)  # NOT NULL
    stock = db.Column(db.Boolean, default=False, nullable=False)  # NOT NULL
    tags = db.Column(db.Boolean, default=False)
    categories = db.Column(db.String(50), nullable=False)  # NOT NULL
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # Clé étrangère
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id')) 