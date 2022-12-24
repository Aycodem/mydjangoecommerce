import requests
# from getpass import getpass


# auth_endpoint='http://localhost:8000/api/products/auth/'
# password=getpass()


# auth_response=requests.post(auth_endpoint,json={'username':'sunday','password':password})


# print(auth_response.json())




endpoint='http://localhost:8000/api/products/'



response=requests.get(endpoint)

print(response.json())