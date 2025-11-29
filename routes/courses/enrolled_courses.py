from models import courseModel,userModel,enrolledModel
from flask_jwt_extended import jwt_required,get_jwt_identity
from flask_smorest import Blueprint,abort
from flask.views import MethodView
from config import db
from sqlalchemy.exc import SQLAlchemyError
from schema import courseSchema,responseSchema,enrolledcourseSchema,enrolledSchema
from flask import request

blp = Blueprint("Enrolled Courses",__name__,description="Operations for users to enroll in courses")

@blp.route("/courses/enrolled")
class course_enrolled(MethodView):
    @jwt_required()
    @blp.response(200,enrolledSchema(many=True))
    def get(self):
        user_id=get_jwt_identity()
        required_courses=enrolledModel.query.filter(enrolledModel.user_id==user_id,enrolledModel.is_enroll==True).all()
        return required_courses
    
@blp.route("/courses/enrolled/<string:course_id>")
class course_enrolled_id(MethodView):
    @jwt_required()
    @blp.response(200,enrolledSchema)
    def get(self,course_id):
        user_id=get_jwt_identity()
        course=enrolledModel.query.filter(enrolledModel.user_id==user_id,enrolledModel.course_id==course_id,enrolledModel.is_enroll==True).first()
        return course
    
    @jwt_required()
    @blp.response(201,responseSchema)
    def post(self,course_id):
        user_id=get_jwt_identity()

        is_exist=enrolledModel.query.filter(enrolledModel.user_id==user_id,enrolledModel.course_id==course_id).first()
        enroll_course=enrolledModel(user_id=user_id,course_id=course_id,is_enroll=True)

        if is_exist:
            abort(500,message="course already enrolled")
        db.session.add(enroll_course)
        db.session.commit()
        return {"message":"course enrolled successfully !!"}