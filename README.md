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

1. Set Environment variables
    You need to set the following Environment variables. The keys needs to be exactly as written here, the vaules can be anything.
    How to set Environment variables is described here: https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html

    * MySQLPassword
    * CustomerSecret

1. Clone the repository from github so you get all the necessary files

    ```shell
    git clone https://github.com/DAT210/Customer.git
    cd Customer/
    docker-compose up --build
    ```

    * If you are using docker toolbox, the address is  http://192.168.99.100:5052/
    * If you are using the new docker, the address is  http://127.0.0.1:5052/

1. You are ready to go!

> Note: If you change anything in the files of the composer, you need to stop the container and run it again for the changes to take effect.

&nbsp;

### Useful for testing

* If you want to reset the database, use these commands:
    ```shell
    docker-compose down -v
    docker-compose up --build
    ```
* If you want to query directly into the database use this command, then treat it like you are using SQL statements.
    > Note: The container you started in step 2 must be running before executing this command.

    ```shell
    docker exec -it customer_db_1 mysql -uroot -p
    ```

## API Reference

With our Api you can get the name, email and Customer Identification Number(cid) of the customer, more will come in the future.

> If you really want to get quickly started see our [full example here](docs/usage.md#full-example).

Everything you need is in the [API docs](docs/).

How to use the API is here: [Usage](docs/usage.md).

### Very brief about how to use the API

In order to obtain information about the Customer, send a get-request with the authorization header you got from the client as a authorization header(how to do that is in Usage docs linked above). Use the base address in the "setting up dev" section with one of the following URIs attached:

* /v1/customer/cid
* /v1/customer/email
* /v1/customer/name

> For example, if you are using the new docker, send a get request to 127.0.0.1:5052/v1/customer/cid to get the cid of the currently logged in customer.