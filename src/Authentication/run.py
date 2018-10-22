from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from passlib.context import CryptContext
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.debug = True

#Getting enviroment variables to avoid having secrets in the code base
EnvVars = os.environ

#Checking if the Enviroment variables exist, and uses them to connect to database. If they were not found, uses default values
if "MySQLUserName" in EnvVars and "MySQLPassword" in EnvVars:
    mysqlAddress = "mysql+pymysql://" + EnvVars["MySQLUserName"] + ":" + EnvVars["MySQLPassword"] + "@127.0.0.1:3352/customer"
else:
    print("WARNING: \"MySQLUserName\" and \"MySQLPassword\" environment variables are not set! See the docs for information. Using the default username and password(unsecure!)")
    mysqlAddress = "mysql+pymysql://root:password@127.0.0.1:3352/customer"

api = Api(app)

#Setting up sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = mysqlAddress
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Checking if the Enviroment variable exist, and uses that as secret. If they were not found, uses default value
if "CustomerApiSecret" in EnvVars:
    app.config['SECRET_KEY'] = EnvVars["CustomerApiSecret"]
else:
    print("WARNING: You need to set the \"CustomerApiSecret\" environment variable, see the docs for information. Using the default secret(unsecure!)")
    app.config['SECRET_KEY'] = "default-secret-key"

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

#Adding jwt
## Checking if the Enviroment variable exist, and uses that as secret. If they were not found, uses default value
if "CustomerJWTSecret" in EnvVars:
    app.config['SECRET_KEY'] = EnvVars["CustomerJWTSecret"]
else:
    print("WARNING: You need to set the \"CustomerJWTSecret\" environment variable, see the docs for information. Using the default secret(unsecure!)")
    app.config['SECRET_KEY'] = "default-jwt-secret-key"

jwt = JWTManager(app)

#Setting up blacklist
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return models.RevokedTokenModel.is_jti_blacklisted(jti)


# Setting up passlib
## Making a CryptoContext which is used for password hashing
pwd_context = CryptContext(
    # Shcemes secify which hashing algorithm(s) we use
    ## We will use argon2, which is relatively new, and very secure. 
    ## CryptContext has support for multiple hashes to be used like this: shcemes = ["default", "legacy_read_only"]
    schemes = ["argon2"],

    #Deprecated="auto" will mark all but the default hash as deprecated
    deprecated="auto"
)

import views, models, resources

# Adding routes for registration and login and other stuff
## These are located in the resources file
api.add_resource(resources.CustomerRegistration, '/registration')
api.add_resource(resources.CustomerLogin, '/login')
api.add_resource(resources.CustomerLogoutAccess, '/logout/access')
api.add_resource(resources.CustomerLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.AllCustomers, '/customers')
api.add_resource(resources.GetCid, '/get-cid')

# Not sure what to do with this yet...
api.add_resource(resources.SecretResource, '/secret')

if __name__ == '__main__':
    app.run(debug=True)

