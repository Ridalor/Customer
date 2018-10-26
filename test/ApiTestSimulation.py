from flask import Flask, request, jsonify
import requests
import sys
from flask_jwt_extended import get_raw_jwt
import json

app = Flask(__name__)
app.debug = True

def get_headers():
    return {"Authorization": request.headers.get("Authorization")}

@app.route('/cid', methods=["GET"])
def hello_world():
    try:
        r = requests.get("http://127.0.0.1:5000/v1/customer/cid", headers=get_headers())
        return jsonify(r.json())
    except Exception as err:
        print(err, file= sys.stderr)
        return "Something went wrong", 500


if __name__ == "__main__":
    app.run(port=5053)