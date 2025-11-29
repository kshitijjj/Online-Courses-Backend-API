from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from config import db,Config,Smorest
import models
from routes.courses.add_to_cart_courses import blp as atccoursesblueprint
from routes.courses.enrolled_courses import blp as enrollcoursesblueprint
from routes.courses.all_courses import blp as allcoursesblueprint
from routes.auth import blp as authblueprint
from routes.instructor import blp as instructorblueprint

jwt=JWTManager()

def create_app():
    app=Flask(__name__) 
    app.config.from_object(Config)
    app.config.from_object(Smorest)

    api = Api(app)
    
    db.init_app(app)
    jwt.init_app(app)   

    api.register_blueprint(authblueprint)
    api.register_blueprint(allcoursesblueprint)
    api.register_blueprint(atccoursesblueprint)
    api.register_blueprint(enrollcoursesblueprint)
    api.register_blueprint(instructorblueprint)

    with app.app_context():
        db.create_all()

    return app

if __name__=="__main__":
    app=create_app()
    app.run(debug=True)
