from config import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash

class userModel(db.Model):
    __tablename__="users"

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),unique=True,nullable=False)
    email=db.Column(db.String,unique=True,nullable=False)
    password=db.Column(db.String,nullable=False)
    role=db.Column(db.String(80),nullable=False,unique=False)
    is_admin=db.Column(db.Boolean,default=False,nullable=False)
    created_at=db.Column(db.DateTime,default=datetime.utcnow)
    enroll=db.relationship("enrolledModel",back_populates="user",lazy="dynamic")
    course=db.relationship("courseModel",back_populates="user",lazy="dynamic")

    def generate_password(self,password):
        self.password=generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password,password)
