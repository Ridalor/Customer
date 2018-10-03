from flask import Flask
from flask_restful import Api
import views, models, resources
from flask_jwt_extended import JWTManager

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

#Adding jwt
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)

#Adding routes for registration and login and other stuff
api.add_resource(resources.CustomerRegistration, '/registration')
api.add_resource(resources.CustomerLogin, '/login')
api.add_resource(resources.CustomerLogoutAccess, '/logout/access')
api.add_resource(resources.CustomerLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.AllCustomers, '/customers')
api.add_resource(resources.SecretResource, '/secret')

#Setting up sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some-secret-string'

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()