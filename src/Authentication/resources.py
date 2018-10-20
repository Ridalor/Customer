from flask_restful import Resource, reqparse
from models import Customer, RevokedTokenModel
import random
import json

from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

parser = reqparse.RequestParser()
parser.add_argument('email', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)


class CustomerRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        # Hashing password as soon as possible, Please dont add anything between the line above and below this comment
        data["password"] = Customer.generate_hash(data["password"])

        # Checking if the email is already in our database, returns message if it is. Countinues if not.
        if Customer.find_by_email(data['email']):
          return {'message': 'User {} already exists'. format(data['email'])}

        #TODO: Improve this \/
        cid = random.randint(10000000, 99999999)
        while Customer.find_by_cid(cid):
            cid += 1
        
        # Making a new model with the email and password provided
        new_customer = Customer(
            customer_id = cid,
            customer_email = data['email'],
            customer_password = data["password"]
        )
        try:
            # Saving the new user to the database. the method is located in models.py
            new_customer.save_to_db()

            # Making tokens so the customer is logged in
            access_token = create_access_token(identity = data['email'])
            refresh_token = create_refresh_token(identity = data['email'])

            return {
                'message': 'Customer {} was created'.format( data['email']),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        except Exception as err:
            return {'message': 'Something went wrong', "error": str(err)}, 500

class CustomerLogin(Resource):
    def post(self):
        data = parser.parse_args()

        # Finding customer from the database
        current_customer = Customer.find_by_email(data['email'])
        if not current_customer:
            return {'message': 'User {} doesn\'t exist'.format(data['email'])}
        
        # Checking password, if correct, it makes tokens to log the customer in
        if Customer.verify_hash(data["password"], current_customer.password):
            access_token = create_access_token(identity = data['email'])
            refresh_token = create_refresh_token(identity = data['email'])
            return {
                'message': 'Logged in as {}'.format(current_customer.email),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        else:
            return {'message': 'Wrong email or password'}

class CustomerLogoutAccess(Resource):
    # Requires a jwt object to run, which basically means that the customer must be logged in to log out(which makes sense)
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}
        except Exception as err:
            return {'message': 'Something went wrong', "error": str(err)}, 500

class CustomerLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': 'Refresh token has been revoked'}
        except Exception as err:
            return {'message': 'Something went wrong', "error": str(err)}, 500

class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity = current_user)
        return {'access_token': access_token}



#Only for testing purposes
## TODO: (IMPORTANTE) Delete "AllCustomers" class before production!
class AllCustomers(Resource):
    def get(self):
        return Customer.return_all()
    
    def delete(self):
        print("Got into delete")
        return Customer.delete_all()

#Currently for testing only
class SecretResource(Resource):
    @jwt_required
    def get(self):
        return {
            "answer": 42
        }

class GetCid(Resource):
    @jwt_required
    def get(self):
        current_customer = get_jwt_identity()
        try:
            customer_object = Customer.find_by_email(current_customer)
            return {"cid": customer_object.cid}
        except Exception as err:
            return {"message": "Something went wrong on the server", "error": str(err)}, 500