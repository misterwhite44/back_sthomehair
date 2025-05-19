from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_restx import fields
from flask_cors import CORS

cors = CORS()


db = SQLAlchemy()
api = Api()
