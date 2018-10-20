# Customer Api Documentation

Welcome to the documentation for Customer Api. 

Full example to quickly get started at the bottom or click here: [Full example](#fullExample)

## Getting information about the Customer

In order to get information about the customer, send a request with the raw jwt object(which is sent by the client).

* Requests are covered below.

* To send the jwt along with the request take the jwt object named "jti" and send it as data in the request.

* JWT Example in python with flask:
    ```python
    import requests
    from flask_jwt_extended import get_raw_jwt

    def main():
        jti = get_raw_jwt()["jti"]
        r = requests.get(address, {"jti": jti})
    ```

If there is no jwt, or the jwt is invalid, the response will be 404 Not Found

### Get the Customer Identification Number (cid) of the currently logged in customer
To get the cid of a customer, simply send a get request to the docker url specified at the top with this behind: /customer/email
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
           "err": (Exception as a string)
       }
    ```


* Example:

```python
import requests
from flask_jwt_extended import get_raw_jwt

def get_cid():
    jti = get_raw_jwt()

    r = requests.get("127.0.0.1:5052/customer/cid", {"jti": jti})
    
    if r.status() != 200:
        return -1
    
    print(r.json()["message"])
    > "Cid for the current customer was found"
    
    cid = r.json()["cid"]
    return cid

    > 40129339

```

### Get the email of the currently logged in customer
To get the email of the currently logged in user, send a get request to the docker url specified at the top with this behind: /customer/email

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
           "err": (Exception as a string)
       }
    ```

* Example in python:
```python
import requests
from flask_jwt_extended import get_raw_jwt

def get_email():
    jti = get_raw_jwt()["jti"]
    
    r = requests.get("127.0.0.1:5052/customer/email", {"jti": jti})
    
    if r.status() != 200:
        return -1
    
    print(r.json()["message"])
    > "Email of current Customer was found"
    
    email = r.json()["email"]
    return email

    > "TestCustomer1@test.com"

```

### Get the Name of the currently logged in customer
To get the name of the currently logged in customer, send a get request to the docker url specified at the top with this behind: /customer/email.
If the Customer does not have a first and/or last name, it will be an empty string

#### Returns

* On success, the status code is 200 and you get this json object: 
    The Customer does have a first name, but do not have a last name
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
           "err": (Exception as a string)
       }
    ```

* Example in python:
```python
import requests
from flask_jwt_extended import get_raw_jwt

def get_name():
    jti = get_raw_jti()["jti"]
    
    r = requests.get("127.0.0.1:5052/customer/name", {"jti": jti})
    
    if r.status() != 200:
        return -1
    
    print(r.json()["message"])
    > "The Name of the current customer was found"

    name["firstName"] = r.json()["firstName"]
    name["lastName"] = r.json()["lastName"]
    return name

    > {"firstName": <first name>, "lastName": <last name>}

```

## <a name="fullExample"></a> Full example

Here is a full example of how to send requests to our Api

```python
import requests
from flask_jwt_extended import get_raw_jwt


def get_cid():
    r = requests.get("127.0.0.1:5052/customer/cid", {"jti": get_raw_jwt()})
    
    if r.status() == 500:
        return "Server error"
    else if r.status() == 404:
        return "Noone is logged in"
    
    print(r.json()["message"])
    > "Cid for the current customer was found"
    
    cid = r.json()["cid"]
    return cid


def get_email():
    r = requests.get("127.0.0.1:5052/customer/email", {"jti": get_raw_jwt()})
    
    if r.status() == 500:
        return "Server error"
    else if r.status() == 404:
        return "Noone is logged in"

    print(r.json()["message"])
    > "Email of current Customer was found"
    
    email = r.json()["email"]
    return email


def get_name():
    r = requests.get("127.0.0.1:5052/customer/name", {"jti": get_raw_jwt()})
    
    if r.status() == 500:
        return "Server error"
    else if r.status() == 404:
        return "Noone is logged in"
    
    print(r.json()["message"])
    > "The Name of the current customer was found"

    name["firstName"] = r.json()["firstName"]
    name["lastName"] = r.json()["lastName"]
    return name

def main():
    cid = get_cid()
    > 40129339

    email = get_email()
    > "TestCustomer1@test.com"

    name = get_name()
    > {"firstName": "Test", "lastName": "Customer"}

```
