from flask import Flask, request
import requests

app = Flask(__name__)

def get_headers():
    return {"Authorization": request.headers.get("Authorization")}

@app.route("/cid")
def get_cid():
    # Sending the get-request with the header required
    r = requests.get("127.0.0.1:5052/v1/customer/cid", headers=get_headers())
    
    # If the status code is 500, an error on our part occured
    if r.status() == 500:
        return r.json() # Contains "message" and "error" which tell you what happened

    #If the status code is 401, there is no logged in customer or the jwt sent is invalid
    elif r.status() == 401:
        return "Noone is logged in"
    
    # The message is recieved with every request and tell you what happened
    print(r.json()["message"])
    # "Cid for the current customer was found"
    
    # The cid from the response is gotten like this
    cid = r.json()["cid"]
    return cid

@app.route("/email")
def get_email():
    # Sending the get-request with the header required
    r = requests.get("127.0.0.1:5052/v1/customer/email", headers=get_headers())
    
    # If the status code is 500, an error on our part occured
    if r.status() == 500:
        return r.json() # Contains "message" and "error" which tell you what happened

    #If the status code is 401, there is no logged in customer or the jti sent is invalid
    elif r.status() == 401:
        return "Noone is logged in"

    # The message is recieved with every request and tell you what happened
    print(r.json()["message"])
    # "Email of current Customer was found"
    
    # The email from the response is gotten like this
    email = r.json()["email"]
    return email

@app.route("/name")
def get_name():
    # Sending the get-request with the header required
    r = requests.get("127.0.0.1:5052/v1/customer/name", headers=get_headers())
    
    # If the status code is 500, an error on our part occured
    if r.status() == 500:
        return r.json() # Contains "message" and "error" which tell you what happened

    #If the status code is 401, there is no logged in customer or the jti sent is invalid
    elif r.status() == 401:
        return "Noone is logged in"
    
    # The message is recieved with every request and tell you what happened
    print(r.json()["message"])
    # "The Name of the current customer was found"

    # The name consist of firstName and Last name, we can organize them in a dict like this
    name["firstName"] = r.json()["firstName"]
    name["lastName"] = r.json()["lastName"]
    return name

if __name__ == "__main__":
    app.run(port=5002)