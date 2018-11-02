import requests

data = [
    {"email": "email1@email.com", "password": "password1"},
    {"email": "email2@email.com", "password": "password2"},
    {"email": "email3@email.com", "password": "password3"},
    {"email": "test@hotmail.com", "password": "test"},
    {"email": "user@gmail.com", "password": "userpass"},
    {"email": "customer@email.com", "password": "password"},
    {"email": "123@email.com", "password": "pwd456"},
    {"email": "example@hotmail.com", "password": "123456789"},
    {"email": "hotmail@hotmail.com", "password": "hotmail"},
    {"email": "gmail@gmail.com", "password": "gmail"}
]

print("Adding example data.")
for payload in data:
    r = requests.post("http://app/v1/registration", data=payload)
    print(r.text)
    