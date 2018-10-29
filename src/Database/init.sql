CREATE DATABASE IF NOT EXISTS customer;

USE customer;

CREATE TABLE IF NOT EXISTS customer_table (
  customer_id int(16) NOT NULL,
  customer_email varchar(128) NOT NULL,
  first_name varchar(128) DEFAULT NULL,
  last_name varchar(128) DEFAULT NULL,
  customer_password varchar(93) DEFAULT NULL,
  address varchar(128) DEFAULT NULL,
  PRIMARY KEY (customer_id),
  UNIQUE KEY Cemail_UNIQUE (customer_email)
);

CREATE TABLE IF NOT EXISTS revoked_tokens (
  id int(11) NOT NULL AUTO_INCREMENT,
  jti varchar(128) DEFAULT NULL,
  PRIMARY KEY (id)
);
