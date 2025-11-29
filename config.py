import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI=os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    JWT_SECRET_KEY=os.getenv("JWT_SECRET_KEY")

class Smorest:
    API_TITLE="Online Courses Backend API"
    API_VERSION="v1"
    OPENAPI_VERSION="3.0.2"
    OPENAPI_URL_PREFIX="/"
    OPENAPI_SWAGGER_UI_PATH="/swagger-ui"
    OPENAPI_SWAGGER_UI_URL="https://cdn.jsdelivr.net/npm/swagger-ui-dist/"