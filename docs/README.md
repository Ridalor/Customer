# Customer Api Documentation

Welcome to the documentation for Customer Api. 

## Getting information about the Customer
### Get the Customer Identification Number (cid)
To get the cid of a customer, simply send a get request to this address: 127.0.0.1:5052/customer/cid.
The number you get is between 8 and 16 digits long.

Example:
* 
```python
import requests

def get_cid():
    r = requests.get("127.0.0.1:5052/customer/cid")
    cid = r.json()["cid"]
    print(cid)
    
> 40129339
```
