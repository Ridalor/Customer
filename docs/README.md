# Customer Api Documentation

Welcome to the documentation for Customer Api. 

__Full example to quickly get started at the bottom or click [here](#fullExample)__

__Base address__
* If you are using docker toolbox: http://192.168.99.100:5052/
* If you are using the new docker: http://127.0.0.1:5052/

## Getting information about the Customer

> When a customer logs in, a jwt-object is sent to and stored on the client(device of the customer). In order for us to give you information about that Customer, we need the JWT-object to identify the Customer and confirm that they are logged in. 

In order to get information about the customer, send a request with the raw jwt object(which is sent by the client).

* The different Requests are covered below.

* To send the jwt along with the request take the jwt object named "jti" and send it as data in the request.

* JWT Example in python with flask:
    ```python
    import requests
    from flask_jwt_extended import get_raw_jwt

    def main():
        jti = get_raw_jwt()["jti"]
        r = requests.get(address, {"jti": jti})
    ```

    > If there is no jwt, or the jwt is invalid, the response will be 404 Not Found

### Get the Customer Identification Number (cid) of the currently logged in customer
URI: /customer/cid
To get the cid of a customer, send a get request to the docker url specified at the top with this URI: /customer/cid
The number you get is between 8 and 16 digits long.

* On success, the status code is 200 and you get this json object: 
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
           "err": "Some error occured"
       }
    ```


* Example:

```python
import requests
from flask_jwt_extended import get_raw_jwt

def get_cid():
    # Getting the jwt with the customer identifier
    jti = get_raw_jwt()

    # Sending the get-request with jti
    r = requests.get("127.0.0.1:5052/customer/cid", {"jti": jti})
    
    # If the status code is 500, an error on our part occured
    if r.status() == 500:
        return "Server error"
    #If the status code is 404, there is no logged in customer or the jti sent is invalid
    else if r.status() == 404:
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
URI: /customer/email
To get the email of the currently logged in user, send a get request to the docker url specified at the top with this URI: /customer/email

#### Returns:
* On success, the status code is 200 and you get this json object: 
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
           "err": "Some error occured"
       }
    ```

* Example in python:
```python
import requests
from flask_jwt_extended import get_raw_jwt

def get_email():
    # Getting the jwt with the customer identifier
    jti = get_raw_jwt()["jti"]
    
    # Sending the get-request with jti
    r = requests.get("127.0.0.1:5052/customer/email", {"jti": jti})
    
    # If the status code is 500, an error on our part occured
    if r.status() == 500:
        return "Server error"
    #If the status code is 404, there is no logged in customer or the jti sent is invalid
    else if r.status() == 404:
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
URI: /customer/name
To get the name of the currently logged in customer, send a get request to the docker url specified at the top with this URI: /customer/name.

If the Customer does not have a first and/or last name, it will be an empty string

#### Returns

* On success, the status code is 200 and you get this json object:

    In this example the Customer have a first name, but do not have a last name
    ```json
       {
           "message": "The Name for the current customer was found",
           "fistName": "Test",
           "lastName": ""
       }
    ```
* On failure on the server, the status code is 500, and you get this json object:

    ```json
       {
           "message": "Something went wrong on the server", 
           "err": "Some error occured"
       }
    ```

* Example in python:
```python
import requests
from flask_jwt_extended import get_raw_jwt

def get_name():
    jti = get_raw_jti()["jti"]
    
    # Sending the get-request with jti
    r = requests.get("127.0.0.1:5052/customer/name", {"jti": jti})
    
    # If the status code is 500, an error on our part occured
    if r.status() == 500:
        return "Server error"
    #If the status code is 404, there is no logged in customer or the jti sent is invalid
    else if r.status() == 404:
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
<a name="fullExample"></a>

## Full example

Here is a full example of how to send requests to our Api:

```python
import requests
from flask_jwt_extended import get_raw_jwt


def get_cid():
    # Sending the get-request with jti
    r = requests.get("127.0.0.1:5052/customer/cid", {"jti": get_raw_jwt()})
    
    # If the status code is 500, an error on our part occured
    if r.status() == 500:
        return "Server error"
    #If the status code is 404, there is no logged in customer or the jti sent is invalid
    else if r.status() == 404:
        return "Noone is logged in"
    
    # The message is recieved with every request and tell you what happened
    print(r.json()["message"])
    > "Cid for the current customer was found"
    
    # The cid from the response is gotten like this
    cid = r.json()["cid"]
    return cid


def get_email():
    # Sending the get-request with jti
    r = requests.get("127.0.0.1:5052/customer/email", {"jti": get_raw_jwt()})
    
    # If the status code is 500, an error on our part occured
    if r.status() == 500:
        return "Server error"
    #If the status code is 404, there is no logged in customer or the jti sent is invalid
    else if r.status() == 404:
        return "Noone is logged in"

    # The message is recieved with every request and tell you what happened
    print(r.json()["message"])
    > "Email of current Customer was found"
    
    # The email from the response is gotten like this
    email = r.json()["email"]
    return email


def get_name():
    # Sending the get-request with jti
    r = requests.get("127.0.0.1:5052/customer/name", {"jti": get_raw_jwt()})
    
    # If the status code is 500, an error on our part occured
    if r.status() == 500:
        return "Server error"
    #If the status code is 404, there is no logged in customer or the jti sent is invalid
    else if r.status() == 404:
        return "Noone is logged in"
    
    # The message is recieved with every request and tell you what happened
    print(r.json()["message"])
    > "The Name of the current customer was found"

    # The name consist of firstName and Last name, we can organize them in a dict like this
    name["firstName"] = r.json()["firstName"]
    name["lastName"] = r.json()["lastName"]
    return name

def main():
    # Use the functions above to get the information
    cid = get_cid()
    > 40129339

    email = get_email()
    > "TestCustomer1@test.com"

    name = get_name()
    > {"firstName": "Test", "lastName": "Customer"}

```
