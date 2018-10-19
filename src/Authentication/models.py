from run import db
from run import pwd_context

class Customer(db.Model):

    cid = db.Column(db.Integer, primary_key = True, nullable = False)
    email = db.Column(db.String(128), unique = True, nullable = False)
    password = db.Column(db.String(128), unique = False, nullable = True)

    firstName = db.Column(db.String(128), unique = False, nullable = True)
    lastName = db.Column(db.String(128), unique = False, nullable = True)

    @staticmethod
    def generate_hash(password):
        return pwd_context.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return pwd_context.verify(password, hash)

    @classmethod
    def find_by_cid(cls, cid):
        return cls.query.filter_by(cid = cid).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email = email).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # TODO: Remove this method before production!
    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'email': x.email,
                'firstName': x.firstName,
                'lastName': x.lastName,
                'password': x.password
                }

        return {'customers': list(map(lambda x: to_json(x), Customer.query.all()))}

    # TODO: Remove this method before production!
    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
        except:
            return {'message': 'Something went wrong'}


class RevokedTokenModel(db.Model):
    __tablename__ = 'revoked_tokens'
    id = db.Column(db.Integer, primary_key = True)
    jti = db.Column(db.String(128))
    
    def add(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti = jti).first()
        return bool(query)