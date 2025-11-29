from config import db
import datetime

class enrolledModel(db.Model):
    __tablename__="enrolled"

    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
    course_id=db.Column(db.Integer,db.ForeignKey("courses.id"))
    is_cart=db.Column(db.Boolean,default=False)
    is_enroll=db.Column(db.Boolean,default=False)
    user=db.relationship("userModel",back_populates="enroll")
    course=db.relationship("courseModel",back_populates="enroll")


