![Logo of the project](docs/images/Customer_logo.png)

# Customer &middot; Group 5 &middot; [![Build Status](https://img.shields.io/travis/npm/npm/latest.svg?style=flat-square)](https://travis-ci.org/npm/npm) [![npm](https://img.shields.io/npm/v/npm.svg?style=flat-square)](https://www.npmjs.com/package/npm) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/your/your-project/blob/master/LICENSE)

Welcome to the Customer Database team. We taking care of registering new customers and logging them in, as well as giving other teams information about the Customer.

Note: Everything here is subject to change!

## Getting started
This will come at a later date.

## Developing
### Built with
* Flask 1.0.2
* Flask-SQLAlchemy 2.3.2
    * PyMySQL 0.9.2
* Flask-RESTful 0.3.6
* Flask-JWT-Extended 3.13.1
* passlib 1.7.1
    * argon2-cffi 18.3.0

## Prerequisites
* [Git](https://git-scm.com/downloads)
* [Docker](https://www.docker.com/get-started)

## Setting up Dev
Make sure you have installed Git and Docker before doing the commands below.

* Clone the repository from github so you get all the necessary files

    ```shell
    git clone https://github.com/DAT210/Customer.git
    cd Customer/
    docker-compose up --build
    ```

    * If you are using docker toolbox, the address is  http://192.168.99.100:5052/
    * If you are using the new docker, the address is  http://127.0.0.1:5052/

## Api Reference

With our Api you can registrate, log customers in and get the name, email and Customer Identification Number(cid) of the customer.

__For better explanation and more in-depth usage look at [the Api docs](docs/). If you just want an overview, continue reading.__

In order to obtain information about the Customer, send a get-request with the raw jwt named "jti" as data(how to do that is in docs linked above). Use the base address in the "setting up dev" section with one of the following URIs attached:

For example 127.0.0.1:5052/v1/customer/cid to get the cid of the currently logged in customer.

### Get information about the currently logged in customer

#### Get cid

```
GET     /v1/cid
SEND    NONE
RECIEVE {
            "message": <message>,
            "cid": <cid>
        }
```

#### Get email

```
GET     /v1/email
SEND    NONE
RECIEVE {
            "message": <message>,
            "email": <email>
        }
```

#### Get name

```
GET     /v1/name
SEND    NONE
RECIEVE {
            "message": <message>,
            "firstName": <firstName>,
            "lastName": <lastName>
        }
```
### Registration and login

#### To registrate a new customer

```
POST    /v1/registration
SEND    {
            "email": <email>,
            "password": <password>
        }
RECIEVE {
            "message": <message>,
            "access_token": <access_token>,
            "refresh_token": <refresh_token>
        }
```

#### To log in a customer

```
POST     /v1/login
SEND    {
            "email": <email>,
            "password": <password>
        }
RECIEVE {
            "message": <message>,
            "access_token": <access_token>,
            "refresh_token": <refresh_token>
            
        }
```
#### To log out from access

```
POST     /v1/logout/access
SEND    {
            "Bearer": "access_token <access_token>"
        }
RECIEVE {
            "message": <message>
        }
```

#### To log out from refresh

```
POST     /v1/logout/refresh
SEND    {
            "Bearer": "refresh_token <refresh_token>"
        }
RECIEVE {
            "message": <message>
        }
```

For more information about sending requests and the response look at the docs here: [Api docs](docs/)