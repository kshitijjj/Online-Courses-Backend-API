from models import courseModel,userModel,enrolledModel
from flask_jwt_extended import jwt_required,get_jwt_identity
from flask_smorest import Blueprint,abort
from flask.views import MethodView
from config import db
from sqlalchemy.exc import SQLAlchemyError
from schema import courseSchema,responseSchema,enrolledcourseSchema,enrolledSchema
from flask import request

blp = Blueprint("Add to Cart Courses",__name__,description="Operations for users to add courses in cart")

@blp.route("/courses/add/<string:course_id>")
class course_cart(MethodView):
    @jwt_required()
    @blp.response(200,enrolledSchema)
    def get(self,course_id):
        user_id=get_jwt_identity()
        course=enrolledModel.query.filter(enrolledModel.user_id==user_id,enrolledModel.course_id==course_id,enrolledModel.is_cart==True).first()
        return course

    @jwt_required()
    @blp.response(201,responseSchema)
    def post(self,course_id):
        user_id=get_jwt_identity()

        is_exist=enrolledModel.query.filter(enrolledModel.user_id==user_id,enrolledModel.course_id==course_id).first()
        add_to_cart_course=enrolledModel(user_id=user_id,course_id=course_id,is_cart=True)

        if is_exist:
            abort(500,message="course already enrolled")
        db.session.add(add_to_cart_course)
        db.session.commit()
        return {"message":"course added to cart successfully !!"}

    @jwt_required()
    @blp.response(200,responseSchema)
    def delete(self,course_id):
        user_id=get_jwt_identity()
        course=enrolledModel.query.filter(enrolledModel.user_id==user_id,enrolledModel.course_id==course_id,enrolledModel.is_cart==True).first()
        course.is_cart=False
        db.session.commit()
        return {"message":"course removed from cart successfully !!"}