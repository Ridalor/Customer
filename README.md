![Logo of the project](docs/images/Customer_logo.png)

# Customer &middot; Group 5 &middot; [![Build Status](https://img.shields.io/travis/npm/npm/latest.svg?style=flat-square)](https://travis-ci.org/npm/npm) [![npm](https://img.shields.io/npm/v/npm.svg?style=flat-square)](https://www.npmjs.com/package/npm) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/your/your-project/blob/master/LICENSE)

Welcome to the Customer Database team. We taking care of registering new customers and logging them in, as well as giving other teams information about the Customer.

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

With our Api you can get the name, email and Customer Identification Number(cid) of the customer.

_For in-depth usage of our Api and how to easily get started, look at the docs here: [Api docs](docs/)_

To get information you send a get request with the raw jwt named "jti" as data. Use the base address above with one of the following behind:
For example 127.0.0.1:5052/customer/cid to get the cid of the currently logged in customer.

* /customer
    * /cid
    * /email
    * /name

The request returns a json object with a message and the variable if it was successful.

Example: 
```json
{
    "message": "Cid of the current customer was found",
    "cid": 40129339
}
```

For more information about sending requests and the returns look at the docs here: [Api docs](docs/)