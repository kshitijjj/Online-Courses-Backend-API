from config import db

class courseModel(db.Model):
    __tablename__="courses"

    id=db.Column(db.Integer,primary_key=True)
    course_title=db.Column(db.String,nullable=False)
    price=db.Column(db.Integer,nullable=False)
    total_enrolled=db.Column(db.Integer,nullable=False)
    reviews=db.Column(db.Integer,nullable=False)
    total_lectures=db.Column(db.Integer,nullable=False)
    level=db.Column(db.String,nullable=False)
    content_duration=db.Column(db.Float,nullable=False)
    subject=db.Column(db.String,nullable=False)
    course_by=db.Column(db.Integer,db.ForeignKey("users.id"))
    enroll=db.relationship("enrolledModel",back_populates="course",lazy="dynamic")
    user=db.relationship("userModel",back_populates="course")