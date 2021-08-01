from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id):
    return Donor.query.get(int(id))


class Donor(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), index=True,
                         unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    contact = db.Column(db.String(15), unique=True, nullable=False)
    state = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    pincode = db.Column(db.String(20), nullable=False)
    bloodgroup = db.Column(db.String(5), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    weight = db.Column(db.Integer(), nullable=False)
    gender = db.Column(db.String(7), nullable=False)
    lastdonation = db.Column(db.String(15))

    def __repr__(self):
        return f"User('{self.username}','{self.email}')"
