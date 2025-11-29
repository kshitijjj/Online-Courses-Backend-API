from models import courseModel
from flask_jwt_extended import jwt_required,get_jwt_identity
from flask_smorest import Blueprint,abort
from flask.views import MethodView
from config import db
from sqlalchemy.exc import SQLAlchemyError
from schema import courseSchema,responseSchema,usercourseSchema,enrolledSchema
from utils import instructor_required

blp=Blueprint("Instructor",__name__,description="Operations for instructors")

@blp.route("/instructor/courses")
class instructor_courses(MethodView):
    @jwt_required()
    @instructor_required
    @blp.response(200,courseSchema(many=True))
    def get(self):
        user_id=get_jwt_identity()
        required_courses=courseModel.query.filter(courseModel.course_by==user_id).all()
        return required_courses
    
    @jwt_required()
    @instructor_required
    @blp.arguments(courseSchema)
    @blp.response(201,responseSchema)
    def post(self,course_data):
        user_id=get_jwt_identity()
        new_course=courseModel(
            course_by=user_id,
            **course_data
        )
        try:
            db.session.add(new_course)
            db.session.commit()
            return {"message":"new course posted successfully !!"}
        except SQLAlchemyError as e:
            abort(500,message=str(e))

@jwt_required()
@instructor_required
@blp.route("/instructor/courses/<string:course_id>")
class instructor_course_id(MethodView):
    @jwt_required()
    @instructor_required
    def delete(self,course_id):
        user_id=get_jwt_identity()
        required_course=courseModel.query.filter(courseModel.course_by==user_id,courseModel.id==course_id).first()
        try:
            db.session.delete(required_course)
            db.session.commit()
        except SQLAlchemyError:
            abort(500,message="error in deleting the course")
