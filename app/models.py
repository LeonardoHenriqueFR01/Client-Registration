from app import db, login_manager
from flask_login import UserMixin


login_manager.login_view = 'main.login'

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(350), nullable=False)

    def __repr__(self):
        return f"<user {self.name}, {self.email}>"
    
    def asdict(self):
        return {
            'id':self.id,
            'name':self.name,
            'email':self.email,
        }  

    Avista = db.relationship('Avista', backref=('user'), lazy=True)
    Financia = db.relationship('Financia', backref=('user'), lazy=True)


class Avista(db.Model):
    __tablename__ = 'avista'
    
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(150), nullable=False)
    name_vehicle = db.Column(db.String(150), nullable=False)
    value_vehicle = db.Column(db.Float, nullable=False)
    value_prohibited = db.Column(db.Float, nullable=False) 
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<avista {self.name}, {self.email}>'
    
    def asdict(self):
        return {
            'id':self.id,
            'name':self.name,
            'name_vehicle':self.name_vehicle,
            'value_vehicle':self.value_vehicle,
            'value_prohibited':self.value_prohibited,
            'user_id':self.user_id
        }


class Financia(db.Model):
    __tablename__ = 'financiamento'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(150), nullable=False)
    name_vehicle = db.Column(db.String(150), nullable=False)
    value_vehicle = db.Column(db.Float, nullable=False)
    value_prohibited = db.Column(db.Float, nullable=False) 
    installments = db.Column(db.Integer, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<financia {self.name}, {self.email}>'
    
    def asdict(self):
        return {
            'id':self.id,
            'name':self.name,
            'name_vehicle':self.name_vehicle,
            'value_vehicle':self.value_vehicle,
            'value_prohibited':self.value_prohibited,
            'installments':self.installments,
            'user_id':self.user_id
        }


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
