from models import userModel
from dotenv import load_dotenv
from flask_jwt_extended import create_access_token
from flask_smorest import Blueprint,abort
from flask.views import MethodView
from config import db
from sqlalchemy.exc import SQLAlchemyError
from schema import signupSchema,loginSchema,responseSchema
import os

load_dotenv()
blp=Blueprint("Authentication",__name__,description="For Login and Sign up users")

@blp.route("/signup")
class users_signup(MethodView):
    @blp.arguments(signupSchema)
    @blp.response(201,responseSchema)
    def post(self,user_data):
        if userModel.query.filter(userModel.username==user_data["username"]).first():
            abort(400,message="User with this username already exists !!")
        
        if userModel.query.filter(userModel.email==user_data["email"]).first():
            abort(400,message="user with this email id already exists !!")
        
        new_user=userModel(**user_data)

        if user_data["email"]==os.getenv("admin_email") and user_data["password"]==os.getenv("admin_password"):
            new_user.is_admin=True
            new_user.role="instructor"
        new_user.generate_password(user_data["password"])
        try:
            db.session.add(new_user)
            db.session.commit()
            return {"message":"user signup successfully"},201
        except SQLAlchemyError:
            abort(500,message="Error in signing up user")

@blp.route("/login")
class users_login(MethodView):
    @blp.arguments(loginSchema)
    @blp.response(200,responseSchema)
    def post(self,user_data):
        is_email=userModel.query.filter(userModel.email==user_data['email']).first()
        if not is_email:
            abort(400,message="email id does not exists !!")

        is_password=is_email.check_password(user_data['password'])
        if not is_password:
            abort(404,message="wrong password !!")
        
        if user_data["email"]==os.getenv("admin_email") and user_data["password"]==os.getenv("admin_password"):
            is_email.is_admin=True
            is_email.role="instructor"

        token=create_access_token(identity=str(is_email.id),
                                  additional_claims={"role":is_email.role,
                                                     "is_admin":is_email.is_admin})
        return {"message":"user login successfully","token":token},200

