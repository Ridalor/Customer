from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from passlib.context import CryptContext
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

print("Starting")

api = Api(app)

#Setting up sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3310/customer'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some-secret-string'

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

#Adding jwt
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
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
api.add_resource(resources.CustomerRegistration, '/v1/registration')
api.add_resource(resources.CustomerLogin, '/v1/login')
api.add_resource(resources.CustomerLogoutAccess, '/v1/logout/access')
api.add_resource(resources.CustomerLogoutRefresh, '/v1/logout/refresh')
api.add_resource(resources.TokenRefresh, '/v1/token/refresh')
api.add_resource(resources.AllCustomers, '/v1/customers')
api.add_resource(resources.GetCid, '/v1/customer/cid')
api.add_resource(resources.GetEmail, '/v1/customer/email')
api.add_resource(resources.GetName, '/v1/customer/name')

# Not sure what to do with this yet...
api.add_resource(resources.SecretResource, '/secret')

if __name__ == '__main__':
    app.run(port=5052, host="0.0.0.0", debug=True)

