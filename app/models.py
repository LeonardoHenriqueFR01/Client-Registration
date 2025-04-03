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
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
