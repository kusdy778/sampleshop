from app import db
from app  import login_manager

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    role = db.Column(db.String(15))
    blocked = db.Column(db.Boolean, default=False)
    confirmed = db.Column(db.Boolean, default=False)
    password = db.Column(db.String(20))

    def __init__(self, email, password, nom, prenom, role='CUSTOMER'):
        self.email = email
        self.password = password
        self.nom = nom
        self.prenom = prenom
        self.blocked = False
        self.confirmed = False
        self.role = role


    def get_id(self):
        return str(self.id)

    @login_manager.user_loader
    def load_user(user_id):
        # Logique pour récupérer l'utilisateur à partir de la base de données
        return  User.query.get(int(user_id))


    

