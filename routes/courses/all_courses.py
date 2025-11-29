from models import courseModel,userModel,enrolledModel
from flask_jwt_extended import jwt_required,get_jwt_identity
from flask_smorest import Blueprint,abort
from flask.views import MethodView
from config import db
from sqlalchemy.exc import SQLAlchemyError
from schema import courseSchema,responseSchema,enrolledcourseSchema,enrolledSchema
from flask import request

blp = Blueprint("Courses",__name__,description="Operations for users")

@blp.route("/courses")
class courses(MethodView):
    @jwt_required()
    @blp.response(200,courseSchema(many=True))
    def get(self):
        try:
            all_courses=courseModel.query.all()
            return all_courses
        except SQLAlchemyError:
            abort(400,message="Error in returning the courses")

    @blp.arguments(courseSchema)
    def post(self,course_data):
        price=request.args.get("price")
        subject=request.args.get("subject")
        course_title=request.args.get("course_title")
        level=request.args.get("level")

        query=courseModel.query
        if price in course_data:
            query=query.filter(courseModel.price >= price)
        if subject in course_data:
            subject=subject.lower()
            query=query.filter(courseModel.subject.lower()==subject)
        if level in course_data:
            query=query.filter(courseModel.level==level)
        if course_title in course_data:
            query=query.filter(courseModel.course_title==course_title)

        res=query.all()
        return res   

@blp.route("/courses/<string:course_id>")
class course_id(MethodView):
    @jwt_required()
    @blp.response(200,courseSchema)
    def get(self,course_id):
        course=courseModel.query.get_or_404(course_id)
        return course