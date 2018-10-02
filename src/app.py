from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy



def create_app():
    app = Flask(__name__)
    app.debug = True

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1/db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    db.init_app(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()