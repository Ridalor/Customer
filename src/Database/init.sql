CREATE DATABASE `customer` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;

USE customer;

CREATE TABLE `customer_table` (
  `customer_id` int(16) NOT NULL,
  `customer_email` varchar(128) NOT NULL,
  `first_name` varchar(128) DEFAULT NULL,
  `last_name` varchar(128) DEFAULT NULL,
  `customer_password` varchar(93) DEFAULT NULL,
  `address` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`customer_id`),
  UNIQUE KEY `Cemail_UNIQUE` (`customer_email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `revoked_tokens` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `jti` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


