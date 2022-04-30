from pharmaton import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    posts = db.relationship('Medicine', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.email}')"


class Medicine(db.Model):
    ref_no = db.Column(db.Integer, primary_key=True)
    medname = db.Column(db.String(80), unique=True, nullable=False)
    efficiency = db.Column(db.Integer, nullable=False)
    sideeffect = db.Column(db.String(80), nullable=False)
    typemed = db.Column(db.String(80), nullable=False)
    cmpname = db.Column(db.String(80), nullable=False)
    disease = db.Column(db.String(80), nullable=False)
    expdate = db.Column(db.DateTime(80), nullable=False)
    mfgdate = db.Column(db.DateTime(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Medicine('{self.medname}','{self.sideeffect}','{self.typemed}','{self.cmpname}','{self.disease}')"


class Sales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    does_available = db.Column(db.Integer, nullable=False)
    dose_sale = db.Column(db.Integer, nullable=False)
    medname = db.Column(db.String(70), nullable=False)
    profit = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Sales('{self.medname}')"


class Departure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ref_no = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(70), nullable=False)
    medname = db.Column(db.String(70), nullable=False)
    depid = db.Column(db.Integer, nullable=False)
    vehicleno = db.Column(db.String(70), nullable=False)

    def __repr__(self):
        return f"Departure('{self.medname}','{self.vehicleno}')"


class Add_disease(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    disease = db.Column(db.String(70), nullable=False)

    def __repr__(self):
        return f"Add_disease('{self.disease}')"
