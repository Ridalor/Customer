# How everything works

Keep in mind that a lot can change.

## Registration

The way the registration works is that someone sends a request to us via /v1/registration with email and password(optionally firstName, lastName and address) as json data. Then we check that everything is ok, and if it is, we make a new 8 digit number which is the Customer Identification number, also known as cid. All information that concerns a Customer __MUST__ be tied to cid, do __NOT__ tie information to an email address, name, or any other information of the customer, __ONLY__ the cid. When that cid has been generated, we store that along with the email address and the password, which is hashed. Then we generate a JWT access and refresh tokens and returns them along with a message that tells you what happened. The access token is used to authenticate and give access to information about that customer. Refresh tokens are used to refresh access tokens, and cannot be used to give access to information. This is explained in further detail a bit later.

## Login

Logging in is very similar to registration, but instead of storing the information, we check if the email and passwords match, and if they match we generate a JWT access and refresh token and sends them along with a message.

## Logout

The JWT access token expires after 15 minutes of being generated, and the JWT refresh token expires after 30 days. That means that the customer can be logged in for 30 days before getting logged out. However, we do want the customer to be able to log out if desired, so for that we have a route to /v1/logout/access and /v1/logout/refresh, which as you can probably guess logs a customer out of access and refresh respectively. The way we handle logouts is with a blacklist, so when a request is sent to one of those addresses, the coresponding token is added to the blacklist. Then for every request coming in that requires to be logged in we check if the JWT is in the blacklist, and if it is, it returns with a message: "The token has been revoked", and you dont get any information. 

## Token refresh
    
If an access token is logged out, or expired, the customer is still logged in, but needs a new access token. A request to /v1/token/refresh with the refresh token attached, a new access token is generated and sent back. 

## Getting information

So if you have a system that interacts with customers, lets say Orders or Booking for instance, you probably have information that you would like to store and tie to a customer. How to do this is described in [Usage](/usage.md), you basically store the information in your way, but with the cid in a column in the table. 

When a request for information is recieved, we look at the JWT access token, and if its valid, we get the cid out of that, finds the information requested and send it as a response. 