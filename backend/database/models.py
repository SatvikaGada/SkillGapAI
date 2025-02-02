from flask_sqlalchemy import SQLAlchemy
db= SQLAlchemy()
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),unique=True, nullable=False)
    skills=db.Column(db.Text,nullable=True) #Stores user skills as text

    def __init__(self, name, email, skills=""):
        self.name=name
        self.email=email
        self.skills=skills