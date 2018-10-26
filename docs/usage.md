# How to use the Customer Api 

If you want to start using our Api, here is how to get started.

_If you want to jump to the code example, click [here](#full-example)_

The IP address is as follows:
* If you are using docker toolbox, the address is  http://192.168.99.100:5052/
* If you are using the new docker, the address is  http://127.0.0.1:5052/

## Getting information about the Customer

In order to get information about the customer, send a request with the authorization header(which contains the customer's jwt) from the client request.

> Why? Because when a customer logs in, a jwt-object is sent to and stored on the client(device of the customer). In order for us to give information about that Customer, we need the JWT-object to identify the Customer and confirm that they are logged in. Note: It is possible that in the future, there will be no need to send the header.

* The different Requests are covered below.

* To send the authorization header with the request, make a dict with the authorization from the request you recieved.

* JWT Example in python with flask:
    ```python
    import requests
    from flask import request

    def get_headers():
        return {"Authorization": request.headers.get("Authorization")}

    def main():
        r = requests.get(<address>, headers= get_headers())
    ```

    > If there is no header, or the jwt in the header is invalid, the response will be 401 Not Found, which means that the client is not logged in as.

### Get the Customer Identification Number (cid) of the currently logged in customer
URI: /v1/customer/cid/

To get the cid of a customer, send a get request to the docker url specified at the top with this URI: /v1/customer/cid
The number you get is between 8 and 16 digits long.

> The returned cid is an integer. This cid number below(40129339) is just an example.

* On success, the status code is 201 and you get this json object: 
    ```json
       {
           "message": "Cid for the current customer was found",
           "cid": 40129339
       }
    ```

* On failure on the server, the status code is 500 and you get this json object:
    ```json
       {
           "message": "Something went wrong on the server", 
           "error": "<Error string>"
       }
    ```


* Example:

```python
import requests
from flask import request

def get_headers():
    return {"Authorization": request.headers.get("Authorization")}


def get_cid():
    # Getting the jwt with the customer identifier
    jti = get_raw_jwt()

    # Sending the get-request with header required
    r = requests.get("127.0.0.1:5052/v1/customer/cid", headers=get_headers())
    
    # If the status code is 500, an error on our part occured
    if r.status() == 500:
        return r.json() # Contains "message" and "error" which tell you what happened

    #If the status code is 401, there is no logged in customer or the jwt sent is invalid
    else if r.status() == 401:
        return "Noone is logged in"
    
    # The message is recieved with every request and tell you what happened
    print(r.json()["message"])
    > "Cid for the current customer was found"
    
    # The cid from the response is gotten like this
    cid = r.json()["cid"]
    return cid

    # This is an example cid
    > 40129339

```

### Get the email of the currently logged in customer
URI: /v1/customer/email

To get the email of the currently logged in user, send a get request to the docker url specified at the top with this URI: /v1/customer/email

> The returned email is a string. The email below is just an example

#### Returns:
* On success, the status code is 201 and you get this json object: 
    ```json
       {
           "message": "Email for the current user was found",
           "email": "TestUser1@test.com"
       }
    ```
* On failure on the server, the status code is 500, and you get this json object:
    ```json
       {
           "message": "Something went wrong on the server", 
           "error": "<Error string>"
       }
    ```

* Example in python:
```python
import requests
from flask import request

def get_headers():
    return {"Authorization": request.headers.get("Authorization")}


def get_email():
    # Getting the jwt with the customer identifier
    jti = get_raw_jwt()["jti"]
    
    # Sending the get-request with the header required
    r = requests.get("127.0.0.1:5052/v1/customer/email", headers=get_headers()
    
    # If the status code is 500, an error on our part occured
    if r.status() == 500:
        return r.json() # Contains "message" and "error" which tell you what happened

    #If the status code is 401, there is no logged in customer or the jwt sent is invalid
    else if r.status() == 401:
        return "Noone is logged in"
    
    # The message is recieved with every request and tell you what happened
    print(r.json()["message"])
    > "Email of current Customer was found"
    
    # The email from the response is gotten like this
    email = r.json()["email"]
    return email

    # This is an example email
    > "TestCustomer1@test.com"

```

### Get the Name of the currently logged in customer
URI: /v1/customer/name

To get the name of the currently logged in customer, send a get request to the docker url specified at the top with this URI: /v1/customer/name.

> The returned firstName and LastName are strings. The name below is just an example. If the Customer does not have a first and/or last name, it will be an empty string

#### Returns

* On success, the status code is 201 and you get this json object:

    In this example the Customer have a first name, but do not have a last name
    ```json
       {
           "message": "The Name for the current customer was found",
           "fistName": "Test",
           "lastName": "Customer"
       }
    ```
* On failure on the server, the status code is 500, and you get this json object:

    ```json
       {
           "message": "Something went wrong on the server", 
           "error": "<Error string>"
       }
    ```

* Example in python:
```python
import requests
from flask import request

def get_headers():
    return {"Authorization": request.headers.get("Authorization")}


def get_name():
    jti = get_raw_jti()["jti"]
    
    # Sending the get-request with the header required
    r = requests.get("127.0.0.1:5052/v1/customer/name", headers=get_headers())
    
    # If the status code is 500, an error on our part occured
    if r.status() == 500:
        return r.json() # Contains "message" and "error" which tell you what happened

    #If the status code is 401, there is no logged in customer or the jwt sent is invalid
    else if r.status() == 401:
        return "Noone is logged in"
    
    # The message is recieved with every request and tell you what happened
    print(r.json()["message"])
    > "The Name of the current customer was found"

    # The name consist of firstName and Last name, we can organize them in a dict like this
    name["firstName"] = r.json()["firstName"]
    name["lastName"] = r.json()["lastName"]
    return name

    # This is how it will be displayed
    > {"firstName": <first name>, "lastName": <last name>}

```

## Full example

Here is a full example of how to get information from our Api:
The example assumes you got a request from a client.

```python
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

    #If the status code is 401, there is no logged in customer or the jwt sent is invalid
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

    #If the status code is 401, there is no logged in customer or the jwt sent is invalid
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
```
