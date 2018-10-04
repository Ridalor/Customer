from flask import Flask
from flask_restful import Api
import views, models, resources
from flask_jwt_extended import JWTManager
from passlib.context import CryptContext
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

#Not sure what to do with this...
api.add_resource(resources.SecretResource, '/secret')

#Setting up sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3310/customer'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some-secret-string'

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

#Setting up blacklist(might change to whitelist later)
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return models.RevokedTokenModel.is_jti_blacklisted(jti)


#Setting up passlib
##Making a CryptoContext which is used for password hashing
pwd_context = CryptContext(
    #Shcemes secify which hashing algorithm(s) we use
    ##We will use argon2, which is pretty new, and very secure. It has support for multiple hashes to be used like this: shcemes = ["default", "legacy_read_only"]
    schemes = ["argon2"],

    #Deprecated="auto" will mark all but the default hash as deprecated
    deprecated="auto"
)